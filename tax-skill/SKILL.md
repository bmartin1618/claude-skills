---
name: tax-return-review
description: Comprehensive tax return review system for Forms 1040, 1065, and 1120S. Identifies return type, applies form-specific checklist, and provides detailed review with actionable feedback on errors, compliance issues, and planning opportunities.
license: Complete terms in LICENSE.txt
---

# Tax Return Review Skill

## Overview

This skill provides comprehensive review of tax returns (Forms 1040, 1065, and 1120S) by automatically identifying the form type, applying the appropriate checklist, and delivering a structured review with checkmarks for compliant items and revision notes for issues found.

**Primary Use Case**: Accountants upload a completed tax return PDF, and the skill performs a systematic review against best practices and common error patterns, returning a checklist showing what's correct (✓) and what needs revision (⚠).

---

## Process

### Step 1: Form Identification

When a tax return is uploaded, immediately analyze the document to identify:

**Form Type Detection**:
- **Form 1040** - Individual Income Tax Return
  - Look for: "Form 1040", "U.S. Individual Income Tax Return"
  - Key identifiers: Individual SSN, filing status (Single, MFJ, MFS, HOH)
  - Schedules: A (itemized), B (interest/dividends), C (business), D (capital gains), E (rental/pass-through), SE (self-employment)

- **Form 1065** - Partnership Return
  - Look for: "Form 1065", "U.S. Return of Partnership Income"
  - Key identifiers: Partnership name, EIN, Schedule K-1s for partners
  - Schedules: K (allocations), L (balance sheet), M-1/M-3 (reconciliation)

- **Form 1120S** - S Corporation Return
  - Look for: "Form 1120S", "U.S. Income Tax Return for an S Corporation"
  - Key identifiers: Corporate name, EIN, S Corp checkbox
  - Schedules: K (allocations), L (balance sheet), M-1/M-2 (reconciliation & AAA)

**Tax Year Identification**: Extract the tax year from the return header.

**State Returns**: Note if state returns are included and identify which states.

---

### Step 2: Apply Form-Specific Checklist

Based on form identification, load and apply the appropriate checklist:

#### For Form 1040 (Individual Returns)
Use the comprehensive checklist from **guidelines/1040.md** covering:
- Initial data verification (SSN, filing status, dependents)
- Income verification (W-2s, 1099s, K-1s, business income, capital gains)
- Deduction review (standard vs itemized, Schedule A items, above-the-line)
- Credit review (CTC, EITC, education, retirement savings)
- Tax calculation (AMT, NIIT, Medicare tax, estimated payments)
- State return coordination
- High-risk audit triggers
- Common errors to avoid

**Key Focus Areas**:
- K-1 items properly flowing through (Box 1 → Schedule E, Box 5 → Schedule B, etc.)
- Basis and passive activity limitations applied
- NIIT calculated if MAGI exceeds thresholds ($200k single, $250k MFJ)
- Estimated tax penalty calculated or safe harbor documented

#### For Form 1065 (Partnership Returns)
Use the comprehensive checklist from **guidelines/1065.md** covering:
- Entity information verification
- Book-tax reconciliation (Schedule M-1/M-3)
- Balance sheet (Schedule L) and capital reconciliation (Schedule M-2)
- Income and deduction review (ordinary income, separately stated items)
- Partner capital account maintenance
- Schedule K-1 preparation and accuracy
- Basis tracking for each partner
- Complex issues (disguised sales, hot assets, §704(c), debt allocation)
- State filing requirements

**Key Focus Areas**:
- Capital accounts reconcile to Schedule L equity
- K-1 liabilities total to balance sheet liabilities
- Guaranteed payments properly classified
- Passive vs non-passive activity designation correct
- At-risk and basis limitations applied

#### For Form 1120S (S Corporation Returns)
Use the comprehensive checklist from **guidelines/1120S.md** covering:
- S Corporation status verification
- Book-tax reconciliation (Schedule M-1/M-3)
- AAA account tracking (Schedule M-2)
- Balance sheet accuracy (Schedule L)
- Income and deduction review
- **Reasonable compensation analysis** (critical!)
- 2% shareholder benefit rules
- Schedule K-1 preparation
- Shareholder basis calculations
- Distribution analysis and ordering rules
- Built-in gains tax (if former C corp)
- State compliance

**Key Focus Areas**:
- **Reasonable compensation for officer-shareholders** (most common IRS issue)
- AAA account properly maintained
- Basis limitations applied to losses
- 2% shareholder health insurance in W-2 Box 1
- One class of stock requirement maintained

---

### Step 3: Systematic Review Execution

Review the uploaded return systematically by:

**3.1 Document Analysis**
- Extract all numerical data from forms
- Identify all attached schedules and supporting forms
- Note any missing schedules or forms that should be present
- Review for mathematical accuracy

**3.2 Checklist Application**
Work through each checklist item and categorize as:
- **✓ VERIFIED** - Item is correct and compliant
- **⚠ NEEDS REVIEW** - Issue identified requiring revision
- **? UNABLE TO VERIFY** - Insufficient information in uploaded document
- **N/A** - Not applicable to this return

**3.3 Cross-References & Tie-Outs**
- Verify numbers tie between related schedules
- Check prior year carryforwards if comparable data available
- Confirm totals and subtotals are mathematically correct
- Validate percentages sum to 100% where required

**3.4 High-Risk Area Deep Dive**
Pay special attention to common error-prone areas:
- **1040**: K-1 flow-through items, passive losses, NIIT, AMT
- **1065**: Capital account reconciliation, liability allocation, basis tracking
- **1120S**: Reasonable compensation, AAA tracking, basis limitations

---

### Step 4: Generate Review Report

Provide a comprehensive review report in the following format:

```markdown
# TAX RETURN REVIEW REPORT

## Return Information
- **Form Type**: [1040/1065/1120S]
- **Tax Year**: [Year]
- **Taxpayer/Entity**: [Name from return]
- **Tax ID**: [SSN/EIN - last 4 digits only]
- **Review Date**: [Current date]

---

## SUMMARY

**Overall Status**: [✓ Ready to File / ⚠ Revisions Required / 🔴 Critical Issues Found]

**Items Verified**: [X] of [Y] checklist items
**Issues Identified**: [Z] items requiring attention
**Planning Opportunities**: [A] opportunities noted

---

## DETAILED CHECKLIST RESULTS

### [Category 1 - e.g., Initial Data Verification]
- ✓ Taxpayer information verified
- ✓ Filing status appropriate
- ⚠ Dependent SSN missing for Child #2 → **ACTION: Obtain SSN before filing**
- ✓ Prior year carryforwards applied

### [Category 2 - e.g., Income Verification]
- ✓ W-2 wages match (Box 1: $85,000)
- ⚠ Schedule B not filed despite $2,100 interest income → **ACTION: Complete Schedule B**
- ✓ K-1 items properly placed
- ⚠ Self-employment tax not calculated on Schedule C income → **ACTION: Complete Schedule SE**

[Continue for all applicable categories...]

---

## ISSUES REQUIRING REVISION

### Critical Issues (Must Fix Before Filing)
1. **[Issue Description]**
   - **Location**: [Where in return]
   - **Current**: [What's currently shown]
   - **Correction**: [What it should be]
   - **Impact**: [Tax effect if not corrected]

### Compliance Issues (Should Fix)
[List items that create compliance risk]

### Optimization Issues (Consider Fixing)
[List missed opportunities or suboptimal elections]

---

## HIGH-RISK AREAS REVIEWED

### [Form-Specific Risk Areas]
- [Risk area 1]: ✓ Verified / ⚠ Issue found
- [Risk area 2]: ✓ Verified / ⚠ Issue found

### Audit Trigger Analysis
- [Trigger 1 - e.g., Large charitable contribution]: [Status and notes]
- [Trigger 2 - e.g., Home office deduction]: [Status and notes]

---

## PLANNING OPPORTUNITIES IDENTIFIED

1. **[Opportunity Title]**
   - Description: [What could be optimized]
   - Potential Benefit: [Estimated tax savings or other benefit]
   - Action: [Specific recommendation]

2. **[Next Opportunity]**
   [Details...]

---

## QUALITY CONTROL VERIFICATION

- [ ] All arithmetic verified
- [ ] Year-over-year comparison performed (if prior year available)
- [ ] Effective tax rate calculated: [X]% [✓ Reasonable / ⚠ Outside normal range]
- [ ] Software diagnostics status: [All cleared / X warnings remaining]
- [ ] Required signatures: [✓ Obtained / ⚠ Missing]

---

## RECOMMENDATIONS

**Before Filing**:
1. [Specific action item]
2. [Specific action item]
3. [Specific action item]

**Client Communication**:
- [Discussion points for client]
- [Additional documentation needed]

**Next Year Planning**:
- [Estimated tax payment recommendations]
- [Strategic planning suggestions]

---

## REVIEWER NOTES

[Any additional context, unusual items, or documentation needs]

---

**Review Completed By**: AI Tax Review Skill v1.0
**Confidence Level**: [High/Medium/Low] - based on document clarity and completeness
```

---

## Special Handling Instructions

### When Documents Are Unclear
If critical information cannot be extracted from the uploaded PDF:
- Note the specific item as "? UNABLE TO VERIFY"
- List what additional information is needed
- Provide conditional review assuming item is correct

### Multi-State Returns
When state returns are included:
- Note which states are filed
- Check for common state-specific issues:
  - **California**: Franchise tax, conformity issues
  - **New York**: State modifications, NYC tax
  - **Ohio**: CAT tax, municipal taxes
  - **Texas**: Franchise tax
- Verify state additions/subtractions properly calculated

### Complex or Unusual Items
For sophisticated tax issues:
- Reference relevant tax code sections
- Note if specialist review recommended
- Suggest documentation requirements

---

## Error Detection Patterns

### Common 1040 Errors to Flag
- K-1 items misplaced (Box 1 on Schedule C instead of E)
- Passive losses claimed without documentation
- NIIT not calculated on high-income returns
- Basis limitations not applied to K-1 losses
- State tax refund not included if itemized prior year
- Capital loss carryforward not utilized

### Common 1065 Errors to Flag
- Capital accounts don't sum to Schedule L equity
- Guaranteed payments not deducted on Page 1
- Liability allocations don't total to balance sheet
- Special allocations without substantial economic effect
- Hot asset rules missed on distributions
- State withholding not remitted for nonresident partners

### Common 1120S Errors to Flag
- Officer compensation below $50k for profitable S Corp
- 2% shareholder health insurance not in W-2 Box 1
- AAA reduced below zero by distributions (only losses allowed)
- Basis limitations not applied to losses
- Debt basis claimed for guaranteed loans (must be direct loan)
- State S elections assumed automatic (many states require separate filing)

---

## Quality Standards

### Accuracy Requirements
- All mathematical calculations verified
- All cross-references and tie-outs checked
- Common errors specifically reviewed
- High-risk areas given extra scrutiny

### Documentation Standards
- Clear identification of each issue
- Specific location reference in return
- Actionable correction guidance
- Tax impact quantified where possible

### Professional Standards
- Maintain confidentiality
- Use professional tax terminology
- Cite relevant tax law when appropriate
- Provide practical, implementable recommendations

---

## Example Usage

**Accountant**: [Uploads completed Form 1040 PDF]

**Skill Response**:
```
Analyzing uploaded document...
✓ Form identified: Form 1040 - Individual Income Tax Return
✓ Tax Year: 2024
✓ Taxpayer: [Name]
✓ Schedules detected: C, E, D, SE

Applying Form 1040 comprehensive checklist...
Reviewing 150+ checklist items...

[Generates full review report with specific findings]

Summary: 8 issues identified requiring revision
- 3 Critical (must fix before filing)
- 3 Compliance (should fix)
- 2 Optimization opportunities

Most significant issue: Schedule SE not completed for Schedule C income ($45,000) - 
results in $6,358 understatement of self-employment tax.
```

---

## Integration with Workflow

### Optimal Usage Pattern
1. **Pre-Review**: Run skill before senior reviewer looks at return
2. **Focused Review**: Senior reviewer addresses flagged items
3. **Final Check**: Re-run skill after corrections to verify all issues resolved

### Time Savings
- Typical return review time: 30-45 minutes manual
- Skill review time: 2-3 minutes
- Allows senior reviewer to focus on judgment calls and planning

### Training Tool
- Use skill output to train junior staff on common errors
- Create firm-specific amendments to checklists
- Track error patterns across firm

---

## Continuous Improvement

The skill should be updated annually for:
- Current tax law changes
- New form revisions
- Emerging IRS audit focus areas
- Firm-specific error patterns discovered
- State tax law updates

---

## Limitations & Disclaimers

**This skill provides**:
- Systematic checklist-based review
- Common error detection
- Compliance verification
- Planning opportunity identification

**This skill does NOT replace**:
- Professional judgment
- Client-specific fact analysis
- Complex tax research
- Legal or audit representation

**Professional responsibility remains with the reviewing CPA.**

---

## Technical Notes

### Form Detection Algorithm
1. Parse PDF text content
2. Search for form identifiers in headers
3. Verify with secondary indicators (schedules, terminology)
4. Extract tax year and entity information

### Checklist Application
1. Load appropriate guideline markdown file
2. Parse checklist structure
3. Apply each item to extracted return data
4. Categorize results (verified/needs review/unable to verify/N/A)
5. Generate formatted output

### Quality Assurance
- Cross-reference multiple data points for verification
- Flag inconsistencies automatically
- Provide confidence level for each finding
- Note any limitations in document analysis

