#!/usr/bin/env python3
"""
Tax Return PDF Anonymizer
This script takes a tax return PDF and draws black rectangles over sensitive information
like SSNs, DOBs, EINs, names, and addresses to anonymize them using NLP/NER.
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Tuple, Dict, Set
import fitz  # PyMuPDF

try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False
    print("Warning: spaCy not available. Name and address detection will be limited.")
    print("Install with: pip install spacy && python -m spacy download en_core_web_sm")


class TaxPDFAnonymizer:
    """Anonymizes sensitive information in tax return PDFs using NLP/NER."""
    
    # Regex patterns for sensitive information
    PATTERNS = {
        'ssn': [
            r'\b\d{3}-\d{2}-\d{4}\b',  # Format: XXX-XX-XXXX
            r'\b\d{3}\s\d{2}\s\d{4}\b',  # Format: XXX XX XXXX
        ],
        'ein': [
            r'\b\d{2}-\d{7}\b',  # Format: XX-XXXXXXX
            r'\bEIN[:\s]*\d{2}-\d{7}\b',  # EIN: XX-XXXXXXX
        ],
        'dob': [
            r'\b\d{1,2}/\d{1,2}/\d{4}\b',  # Format: MM/DD/YYYY or M/D/YYYY
            r'\b\d{1,2}-\d{1,2}-\d{4}\b',  # Format: MM-DD-YYYY or M-D-YYYY
            r'\b\d{4}/\d{1,2}/\d{1,2}\b',  # Format: YYYY/MM/DD
            r'\b\d{4}-\d{1,2}-\d{1,2}\b',  # Format: YYYY-MM-DD
            r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}\b',  # Month DD, YYYY
        ],
        'phone': [
            r'\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b',  # Format: XXX-XXX-XXXX, XXX.XXX.XXXX, XXX XXX XXXX
            r'\(\d{3}\)\s*\d{3}[-.\s]\d{4}\b',  # Format: (XXX) XXX-XXXX
            r'\b1[-.\s]\d{3}[-.\s]\d{3}[-.\s]\d{4}\b',  # Format: 1-XXX-XXX-XXXX (with country code)
            r'\+1[-.\s]\d{3}[-.\s]\d{3}[-.\s]\d{4}\b',  # Format: +1-XXX-XXX-XXXX
        ],
        'address': [
            # Street address patterns
            r'\b\d+\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd|Court|Ct|Circle|Cir|Way|Place|Pl|Parkway|Pkwy)\b',
            r'\b\d+\s+[NSEW]\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd)\b',
            # P.O. Box
            r'\bP\.?O\.?\s+Box\s+\d+\b',
            r'\bPost\s+Office\s+Box\s+\d+\b',
            # ZIP codes (be careful not to match other 5-digit numbers)
            r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?,\s*[A-Z]{2}\s+\d{5}(?:-\d{4})?\b',  # City, ST ZIP
        ],
    }
    
    # Words to exclude from name detection (common words that aren't names)
    NAME_EXCLUSIONS = {
        'first', 'last', 'name', 'middle', 'initial', 'taxpayer', 'spouse',
        'employer', 'employee', 'business', 'recipient', 'payer', 'filing',
        'status', 'address', 'city', 'state', 'zip', 'social', 'security',
        'number', 'ssn', 'ein', 'date', 'birth', 'dob', 'phone', 'email',
        'tax', 'form', 'return', 'year', 'income', 'deduction', 'credit',
        'january', 'february', 'march', 'april', 'may', 'june', 'july',
        'august', 'september', 'october', 'november', 'december', 'total',
        'amount', 'paid', 'owed', 'refund', 'balance', 'due', 'page', 'of',
        # Tax form abbreviations and common text
        'sch', 'schedule', 'box', 'line', 'ins', 'int', 'baa', 'eic', 'irs',
        'com', 'day', 'med', 'arc', 'req', 'cov', 'sim', 'roy', 'ali', 'rot',
        'lin', 'sal', 'spo', 'joi', 'fra', 'ent', 'col', 'for', 'tre', 'sto',
        'tac', 'apt', 'w-2', 'k-1', 'www', 'intuit', 'cgm', 'tim', 'tax help',
        'smart work', 'recognized', 'unrecap', 'method', 'simple', 'tribal',
        'gaming', 'coverdell', 'archer', 'reciprocal', 'tribal gaming'
    }
    
    def __init__(self, input_pdf: str, output_pdf: str = None, 
                 redact_ssn: bool = True, redact_ein: bool = True, 
                 redact_dob: bool = False, redact_names: bool = True,
                 redact_addresses: bool = True, redact_phone: bool = True,
                 redact_workplaces: bool = True, use_nlp: bool = True, 
                 padding: int = 2):
        """
        Initialize the anonymizer.
        
        Args:
            input_pdf: Path to input PDF file
            output_pdf: Path to output PDF file (default: input_anonymized.pdf)
            redact_ssn: Whether to redact Social Security Numbers
            redact_ein: Whether to redact Employer Identification Numbers
            redact_dob: Whether to redact Dates of Birth (disabled by default)
            redact_names: Whether to redact names (using NER if available)
            redact_addresses: Whether to redact addresses
            redact_phone: Whether to redact phone numbers
            redact_workplaces: Whether to redact employer/workplace names
            use_nlp: Whether to use NLP/NER for name and address detection
            padding: Padding around redaction boxes in points
        """
        self.input_pdf = Path(input_pdf)
        if not self.input_pdf.exists():
            raise FileNotFoundError(f"Input PDF not found: {input_pdf}")
        
        if output_pdf is None:
            output_pdf = self.input_pdf.parent / f"{self.input_pdf.stem}_anonymized.pdf"
        self.output_pdf = Path(output_pdf)
        
        self.redact_ssn = redact_ssn
        self.redact_ein = redact_ein
        self.redact_dob = redact_dob
        self.redact_names = redact_names
        self.redact_addresses = redact_addresses
        self.redact_phone = redact_phone
        self.redact_workplaces = redact_workplaces
        self.use_nlp = use_nlp and SPACY_AVAILABLE
        self.padding = padding
        
        self.doc = None
        self.redaction_count = 0
        
        # Initialize spaCy model if available and requested
        self.nlp = None
        if self.use_nlp and (self.redact_names or self.redact_addresses):
            try:
                self.nlp = spacy.load("en_core_web_sm")
                print("Using spaCy NER for enhanced name and address detection")
            except OSError:
                print("spaCy model not found. Install with: python -m spacy download en_core_web_sm")
                print("Falling back to regex-based detection")
                self.use_nlp = False
    
    def find_text_instances(self, page, pattern: str) -> List[Tuple[fitz.Rect, str]]:
        """
        Find all instances of a pattern on a page.
        
        Args:
            page: PyMuPDF page object
            pattern: Regex pattern to search for
            
        Returns:
            List of tuples containing (bounding_box, matched_text)
        """
        instances = []
        
        # Get all text from the page
        text = page.get_text("text")
        
        # Find all matches in the text
        for match in re.finditer(pattern, text, re.IGNORECASE):
            matched_text = match.group()
            
            # Use PyMuPDF's search to find bounding boxes
            text_rects = page.search_for(matched_text)
            
            # Add all found instances
            for rect in text_rects:
                instances.append((rect, matched_text))
        
        return instances
    
    def find_entities_with_nlp(self, page) -> Dict[str, List[Tuple[fitz.Rect, str]]]:
        """
        Use spaCy NER to find PERSON and ORG entities on a page.
        Very conservative to avoid false positives.
        
        Args:
            page: PyMuPDF page object
            
        Returns:
            Dictionary with entity types as keys and lists of (bbox, text) tuples as values
        """
        if not self.nlp:
            return {'PERSON': [], 'ORG': []}
        
        entities = {'PERSON': [], 'ORG': []}
        
        # Get text from the page
        text = page.get_text("text")
        
        # Process with spaCy
        doc = self.nlp(text)
        
        # Extract entities with strict filtering
        for ent in doc.ents:
            if ent.label_ not in entities:
                continue
                
            entity_text = ent.text.strip()
            entity_lower = entity_text.lower().strip()
            
            # Check if the entity is in our exclusion list
            if entity_lower in self.NAME_EXCLUSIONS:
                continue
            
            # Skip very short entities (likely abbreviations or fragments)
            if len(entity_text) <= 3:
                continue
            
            # Skip if it's just numbers
            if entity_text.replace(',', '').replace('.', '').replace('-', '').replace('$', '').isdigit():
                continue
            
            # Skip if it's very short and all caps (likely abbreviation)
            if len(entity_text) <= 5 and entity_text.isupper():
                continue
            
            # Skip if starts with common form prefixes
            if any(entity_text.startswith(prefix) for prefix in 
                   ['Schedule ', 'Box ', 'Line ', 'Form ', 'Page ', 'Section ', 'Part ', 'Worksheet ']):
                continue
            
            # Skip website domains
            if '.' in entity_text and ('www' in entity_lower or '.com' in entity_lower or 
                                       '.gov' in entity_lower or '.org' in entity_lower):
                continue
            
            # PERSON-specific filters
            if ent.label_ == 'PERSON':
                # Must have at least one uppercase letter followed by lowercase (proper name format)
                if not any(c.isupper() for c in entity_text):
                    continue
                # Must be at least 4 characters for a name (e.g., "Jane")
                if len(entity_text) < 4:
                    continue
                # Skip single-word names that are less than 5 characters (likely fragments)
                if ' ' not in entity_text and len(entity_text) < 5:
                    continue
                # Skip if it ends with common suffixes that indicate it's not a name
                if any(entity_text.endswith(suffix) for suffix in 
                       [' ins', ' sch', ' int', ' inc', ' llc', ' corp']):
                    continue
            
            # ORG-specific filters (for workplaces)
            if ent.label_ == 'ORG':
                # Must be at least 5 characters
                if len(entity_text) < 5:
                    continue
                # Skip common tax form terms
                if any(term in entity_lower for term in 
                       ['schedule', 'worksheet', 'statement', 'attachment', 'instructions', 
                        'internal revenue', 'department', 'treasury']):
                    continue
            
            # Search for the entity in the PDF
            text_rects = page.search_for(entity_text)
            for rect in text_rects:
                entities[ent.label_].append((rect, entity_text))
        
        return entities
    
    def find_addresses_with_regex(self, page) -> List[Tuple[fitz.Rect, str]]:
        """
        Find addresses using regex patterns.
        Only matches full street addresses, not just city names.
        
        Args:
            page: PyMuPDF page object
            
        Returns:
            List of tuples containing (bounding_box, matched_text)
        """
        instances = []
        
        # Only use street address patterns, not city/state patterns
        # This avoids false positives from state names in forms
        street_patterns = [
            self.PATTERNS['address'][0],  # Street address with number
            self.PATTERNS['address'][1],  # Directional street address
            self.PATTERNS['address'][2],  # P.O. Box
            self.PATTERNS['address'][3],  # Post Office Box
            # Skip the City, ST ZIP pattern as it catches too many false positives
        ]
        
        for pattern in street_patterns:
            found = self.find_text_instances(page, pattern)
            instances.extend(found)
        
        return instances
    
    def draw_redaction_box(self, page, rect: fitz.Rect):
        """
        Draw a black rectangle over the specified area.
        
        Args:
            page: PyMuPDF page object
            rect: Rectangle to redact
        """
        # Add padding
        padded_rect = fitz.Rect(
            rect.x0 - self.padding,
            rect.y0 - self.padding,
            rect.x1 + self.padding,
            rect.y1 + self.padding
        )
        
        # Draw filled black rectangle
        page.draw_rect(padded_rect, color=(0, 0, 0), fill=(0, 0, 0))
        self.redaction_count += 1
    
    def anonymize(self) -> Dict[str, int]:
        """
        Anonymize the PDF by redacting sensitive information.
        
        Returns:
            Dictionary with counts of redacted items by type
        """
        print(f"Opening PDF: {self.input_pdf}")
        self.doc = fitz.open(self.input_pdf)
        
        counts = {
            'ssn': 0,
            'ein': 0,
            'dob': 0,
            'phone': 0,
            'names': 0,
            'addresses': 0,
            'workplaces': 0,
            'total_pages': len(self.doc)
        }
        
        # Process each page
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            print(f"Processing page {page_num + 1}/{len(self.doc)}...")
            
            # Track what we've already redacted to avoid duplicates
            redacted_areas: Set[Tuple[float, float, float, float]] = set()
            
            def add_redaction(bbox, text, category):
                """Helper to add redaction and track it"""
                bbox_tuple = (round(bbox.x0, 2), round(bbox.y0, 2), 
                            round(bbox.x1, 2), round(bbox.y1, 2))
                if bbox_tuple not in redacted_areas:
                    self.draw_redaction_box(page, bbox)
                    redacted_areas.add(bbox_tuple)
                    counts[category] += 1
                    # Show abbreviated version for privacy
                    display_text = text[:10] + "***" if len(text) > 10 else text[:3] + "***"
                    print(f"  Redacted {category}: {display_text}")
            
            # Redact SSNs
            if self.redact_ssn:
                for pattern in self.PATTERNS['ssn']:
                    instances = self.find_text_instances(page, pattern)
                    for bbox, text in instances:
                        add_redaction(bbox, text, 'ssn')
            
            # Redact EINs
            if self.redact_ein:
                for pattern in self.PATTERNS['ein']:
                    instances = self.find_text_instances(page, pattern)
                    for bbox, text in instances:
                        add_redaction(bbox, text, 'ein')
            
            # Redact DOBs
            if self.redact_dob:
                for pattern in self.PATTERNS['dob']:
                    instances = self.find_text_instances(page, pattern)
                    for bbox, text in instances:
                        add_redaction(bbox, text, 'dob')
            
            # Redact phone numbers
            if self.redact_phone:
                for pattern in self.PATTERNS['phone']:
                    instances = self.find_text_instances(page, pattern)
                    for bbox, text in instances:
                        add_redaction(bbox, text, 'phone')
            
            # Redact names using NER
            if self.redact_names:
                if self.use_nlp:
                    entities = self.find_entities_with_nlp(page)
                    for bbox, text in entities['PERSON']:
                        add_redaction(bbox, text, 'names')
            
            # Redact workplaces/employer names using NER
            if self.redact_workplaces:
                if self.use_nlp:
                    entities = self.find_entities_with_nlp(page)
                    for bbox, text in entities['ORG']:
                        add_redaction(bbox, text, 'workplaces')
            
            # Redact addresses (street addresses only, not city names)
            if self.redact_addresses:
                # Use regex patterns for actual street addresses
                address_instances = self.find_addresses_with_regex(page)
                for bbox, text in address_instances:
                    add_redaction(bbox, text, 'addresses')
        
        # Save the anonymized PDF
        print(f"\nSaving anonymized PDF to: {self.output_pdf}")
        self.doc.save(self.output_pdf)
        self.doc.close()
        
        counts['total_redactions'] = self.redaction_count
        return counts
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.doc:
            self.doc.close()


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Anonymize sensitive information in tax return PDFs using NLP/NER',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Anonymize all sensitive information (SSN, EIN, phone, names, addresses, workplaces)
  python remove-sensitive-info.py input.pdf
  
  # Specify output file
  python remove-sensitive-info.py input.pdf -o output.pdf
  
  # Only redact SSNs and names
  python remove-sensitive-info.py input.pdf --no-ein --no-addresses --no-workplaces --no-phone
  
  # Also include dates of birth
  python remove-sensitive-info.py input.pdf --dob
  
  # Disable NLP/NER and use only regex patterns
  python remove-sensitive-info.py input.pdf --no-nlp
  
  # Adjust padding around redaction boxes
  python remove-sensitive-info.py input.pdf --padding 5

Note: For best results with NLP, install spaCy model:
  python -m spacy download en_core_web_sm
        """
    )
    
    parser.add_argument('input_pdf', help='Path to input PDF file')
    parser.add_argument('-o', '--output', help='Path to output PDF file (default: input_anonymized.pdf)')
    parser.add_argument('--no-ssn', action='store_true', help='Do not redact Social Security Numbers')
    parser.add_argument('--no-ein', action='store_true', help='Do not redact Employer Identification Numbers')
    parser.add_argument('--dob', action='store_true', help='Also redact Dates of Birth (disabled by default)')
    parser.add_argument('--no-phone', action='store_true', help='Do not redact phone numbers')
    parser.add_argument('--no-names', action='store_true', help='Do not redact names')
    parser.add_argument('--no-addresses', action='store_true', help='Do not redact addresses')
    parser.add_argument('--no-workplaces', action='store_true', help='Do not redact employer/workplace names')
    parser.add_argument('--no-nlp', action='store_true', help='Disable NLP/NER (use only regex patterns)')
    parser.add_argument('--padding', type=int, default=2, help='Padding around redaction boxes in points (default: 2)')
    
    args = parser.parse_args()
    
    try:
        anonymizer = TaxPDFAnonymizer(
            input_pdf=args.input_pdf,
            output_pdf=args.output,
            redact_ssn=not args.no_ssn,
            redact_ein=not args.no_ein,
            redact_dob=args.dob,  # Changed: only redact if explicitly requested
            redact_names=not args.no_names,
            redact_addresses=not args.no_addresses,
            redact_phone=not args.no_phone,
            redact_workplaces=not args.no_workplaces,
            use_nlp=not args.no_nlp,
            padding=args.padding
        )
        
        counts = anonymizer.anonymize()
        
        print("\n" + "="*50)
        print("ANONYMIZATION COMPLETE")
        print("="*50)
        print(f"Total pages processed: {counts['total_pages']}")
        print(f"SSNs redacted: {counts['ssn']}")
        print(f"EINs redacted: {counts['ein']}")
        print(f"Phone numbers redacted: {counts['phone']}")
        print(f"Names redacted: {counts['names']}")
        print(f"Addresses redacted: {counts['addresses']}")
        print(f"Workplaces redacted: {counts['workplaces']}")
        if counts['dob'] > 0:
            print(f"DOBs redacted: {counts['dob']}")
        print(f"Total redactions: {counts['total_redactions']}")
        print(f"\nOutput saved to: {anonymizer.output_pdf}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing PDF: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
