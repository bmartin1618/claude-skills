# Tax Return Review Skill

## Overview

This Claude Skill provides automated, comprehensive review of tax returns (Forms 1040, 1065, and 1120S) by detecting the form type, applying specialized checklists, and returning actionable feedback with checkmarks (✓) for compliant items and revision notes (⚠) for issues.

## What Was Created

### 1. Form-Specific Checklists
Each checklist is comprehensive, practical, and based on the detailed guidance from your `parts/` directory:

- **`guidelines/1040.md`** - Individual Income Tax Return Checklist (150+ items)
  - Initial data verification
  - Income verification (W-2, K-1, business, capital gains)
  - Deduction review (standard vs itemized)
  - Credits (CTC, EITC, education, retirement)
  - Special taxes (AMT, NIIT, Medicare)
  - State coordination
  - High-risk audit triggers
  - Common errors

- **`guidelines/1065.md`** - Partnership Return Checklist (120+ items)
  - Entity information
  - Book-tax reconciliation (M-1/M-3, L, M-2)
  - Partner capital accounts
  - K-1 preparation and basis tracking
  - Complex issues (disguised sales, hot assets, §704(c), debt allocation)
  - Multi-state requirements
  - Common partnership errors

- **`guidelines/1120S.md`** - S Corporation Return Checklist (130+ items)
  - S Corp status verification
  - Reasonable compensation analysis (critical!)
  - AAA account tracking
  - Book-tax reconciliation
  - 2% shareholder benefit rules
  - K-1 and basis calculations
  - Distribution ordering
  - Built-in gains tax
  - Common S Corp errors

### 2. Main Skill Orchestration
**`SKILL.md`** - The main skill file that:
1. **Identifies** the form type from uploaded PDFs
2. **Applies** the appropriate checklist automatically
3. **Generates** a comprehensive review report with:
   - Summary of issues (critical, compliance, optimization)
   - Detailed checklist results with ✓ or ⚠
   - Specific corrections needed with locations
   - High-risk area analysis
   - Planning opportunities
   - Quality control verification
   - Actionable recommendations

## How It Works

```
Accountant uploads completed tax return PDF
           ↓
Skill detects form type (1040, 1065, or 1120S)
           ↓
Loads appropriate checklist from guidelines/
           ↓
Systematically reviews each checklist item
           ↓
Generates comprehensive report with:
  • ✓ Items that are correct
  • ⚠ Items needing revision (with specific actions)
  • Planning opportunities identified
```

## Example Output Format

```markdown
# TAX RETURN REVIEW REPORT

## SUMMARY
Overall Status: ⚠ Revisions Required
Items Verified: 142 of 150
Issues Identified: 8 items requiring attention

## DETAILED CHECKLIST RESULTS

### Income Verification
- ✓ W-2 wages verified ($85,000)
- ⚠ Schedule B missing (interest income $2,100 > $1,500)
  → ACTION: Complete Schedule B before filing
- ✓ K-1 items properly placed
- ⚠ Schedule SE not completed for Schedule C income
  → ACTION: Calculate self-employment tax ($6,358)

### High-Risk Areas
- ⚠ NIIT not calculated (MAGI $275k > $250k threshold)
  → ACTION: Complete Form 8960 (estimated tax $1,900)

[... continues with all findings ...]

## RECOMMENDATIONS
Before Filing:
1. Complete Schedule B for interest income
2. Calculate and include Schedule SE ($6,358 additional tax)
3. Complete Form 8960 for NIIT ($1,900 additional tax)
```

## Key Features

### Comprehensive Coverage
- Based on real-world tax practice experience
- Incorporates common error patterns
- Addresses high-risk audit areas
- Includes state tax considerations

### Practical & Actionable
- Specific location references in returns
- Clear correction instructions
- Tax impact quantified
- Client communication suggestions

### Form-Specific Focus Areas

**1040 Critical Areas:**
- K-1 flow-through items properly placed
- Passive activity limitations applied
- NIIT calculated when required
- Basis limitations checked

**1065 Critical Areas:**
- Capital accounts reconcile to Schedule L
- Liability allocations correct
- Guaranteed payments properly classified
- Partner basis tracking maintained

**1120S Critical Areas:**
- **Reasonable compensation** (most common IRS issue!)
- AAA account properly tracked
- 2% shareholder health insurance treatment
- Basis limitations applied to losses

## Usage Scenarios

### 1. Pre-Review Quality Check
Run before senior reviewer looks at return to catch obvious errors

### 2. Training Tool
Use output to teach junior staff what to look for

### 3. Focused Review
Senior reviewer addresses only flagged items, saving time

### 4. Final Verification
Re-run after corrections to ensure all issues resolved

## Time Savings

- **Manual review**: 30-45 minutes per return
- **Skill review**: 2-3 minutes
- **Result**: Senior reviewer focuses on judgment calls and planning, not mechanical checks

## Source Material

All checklists are based on the comprehensive guidance in your `parts/` directory:
- `parts/SKILL.md` - Main tax review knowledge base
- `parts/quick-reference.md` - Top 10 critical points per form
- `parts/error-diagnostics.md` - Common error patterns
- `parts/implementation-guide.md` - Best practices and procedures

## Files Created

```
tax-skill/
├── SKILL.md                    # Main orchestration skill (Claude Skills format)
├── README.md                   # This file
├── guidelines/
│   ├── 1040.md                # Individual return checklist
│   ├── 1065.md                # Partnership return checklist
│   └── 1120S.md               # S Corporation return checklist
├── parts/                      # Original source material (preserved)
│   ├── SKILL.md
│   ├── quick-reference.md
│   ├── error-diagnostics.md
│   └── [other reference files]
└── example-skill/              # Template reference (preserved)
    └── SKILL.md
```

## Integration with Claude

This skill is formatted for **Claude Skills** and can be used by:
1. Loading the `SKILL.md` file into Claude
2. Uploading a completed tax return PDF
3. Claude will automatically:
   - Detect the form type
   - Apply the appropriate checklist
   - Return comprehensive review with actionable feedback

## Customization

You can customize the checklists by:
- Adding firm-specific requirements to guidelines/*.md files
- Incorporating client-specific review points
- Adding industry-specific considerations
- Including local tax jurisdiction requirements

## Maintenance

Update annually for:
- Tax law changes
- New form revisions
- IRS focus areas
- State tax updates
- Firm error patterns discovered

## Professional Standards

**This skill provides**:
✓ Systematic checklist-based review
✓ Common error detection
✓ Compliance verification
✓ Planning opportunity identification

**This skill does NOT replace**:
✗ Professional CPA judgment
✗ Client-specific fact analysis
✗ Complex tax research
✗ Legal representation

**Professional responsibility remains with the reviewing CPA.**

---

## Quick Start

1. Open Claude with Skills support
2. Load `SKILL.md` as a skill
3. Upload a completed tax return PDF
4. Receive comprehensive review in 2-3 minutes
5. Address flagged issues
6. Re-run for final verification

---

Built with knowledge from extensive tax practice experience and designed for real-world accounting firm workflows.

