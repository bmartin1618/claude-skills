---
name: tax-return-review
description: Comprehensive tax return review system for Forms 1040, 1065, and 1120S. Identifies return type, applies detailed procedural workflows with step-by-step verification instructions, and provides actionable feedback on errors, compliance issues, and planning opportunities.
license: Complete terms in LICENSE.txt
---

# Tax Return Review Skill

## Overview

This skill provides comprehensive review of tax returns (Forms 1040, 1065, and 1120S) by automatically identifying the form type, following detailed **procedural workflows** (not simple checklists), and delivering a structured review with verification results and specific correction instructions.

**Primary Use Case**: Accountants upload a completed tax return PDF, and the skill executes systematic workflow procedures with explicit step-by-step instructions for each verification, returning detailed findings showing what's correct (✓), what needs revision (⚠), and exactly how to fix issues.

**Key Difference**: These are **workflow guides** with explicit procedures (e.g., "Locate Line 1, extract Box 1 from each W-2, sum amounts, verify equals Line 1"), not simple topic checklists.

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

### Step 2: Load and Execute Form-Specific Workflow

Based on form identification, load and execute the appropriate procedural workflow:

#### For Form 1040 (Individual Returns)
Follow the comprehensive workflow from **reference/1040.md** with **9 detailed procedural steps** covering:
- Initial data verification (SSN, filing status, dependents)
- Income verification (W-2s, 1099s, K-1s, business income, capital gains)
- Deduction review (standard vs itemized, Schedule A items, above-the-line)
- Credit review (CTC, EITC, education, retirement savings)
- Tax calculation (AMT, NIIT, Medicare tax, estimated payments)
- State return coordination
- High-risk audit triggers
- Common errors to avoid

**Workflow Procedures Include**:
- **Step 1.1**: Explicit taxpayer identification verification (locate name, verify SSN format, compare to prior year)
- **Step 2.1**: W-2 reconciliation procedure (extract Box 1 from each W-2, sum, verify equals Line 1)
- **Step 2.5**: K-1 box-by-box placement verification with decision trees
  - Box 1 → Schedule E Part II (NOT Schedule C - common error!)
  - Box 5 → Schedule B (forces Schedule B even if <$1,500)
  - Complete placement guide for all 20 K-1 boxes
- **Basis limitation workflow**: Calculate available basis, test loss against basis, suspend excess
- **Passive activity decision trees**: 7 material participation tests with if-then logic
- **NIIT calculation procedure**: Step-by-step MAGI threshold test, identify investment income, calculate 3.8% tax
- **Pass/Fail criteria** for each verification step

#### For Form 1065 (Partnership Returns)
Follow the comprehensive workflow from **reference/1065.md** with **9 detailed procedural steps** covering:
- Entity information verification
- Book-tax reconciliation (Schedule M-1/M-3)
- Balance sheet (Schedule L) and capital reconciliation (Schedule M-2)
- Income and deduction review (ordinary income, separately stated items)
- Partner capital account maintenance
- Schedule K-1 preparation and accuracy
- Basis tracking for each partner
- Complex issues (disguised sales, hot assets, §704(c), debt allocation)
- State filing requirements

**Workflow Procedures Include**:
- **Step 2.1**: Schedule M-1 line-by-line reconciliation procedure (book income + adjustments = taxable income)
- **Step 2.4**: Schedule M-2 capital account flow verification
  - Beginning (ties to prior) + contributions + income - distributions - losses = ending (ties to Schedule L Line 21)
  - Explicit formula with each component verified
- **Step 5.1**: Partner capital account reconciliation for each partner with calculation worksheet
- **Step 5.3**: K-1 summation verification procedure
  - For EACH line: Sum all K-1s must equal Schedule K
  - Example: All K-1 Box 1 amounts totaled = Schedule K Line 1
- **Step 6.1**: Disguised sales testing (2-year rule with presumptions)
- **Step 6.2**: Hot assets identification and ordinary income calculation
- **Step 6.3**: §704(c) property tracking with three allocation methods
- **Step 6.4**: Liability allocation procedures (recourse: who guarantees? nonrecourse: profit-sharing ratio)
- **Pass/Fail criteria** and verification formulas for each step

#### For Form 1120S (S Corporation Returns)
Follow the comprehensive workflow from **reference/1120S.md** with **10 detailed procedural steps** covering:
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

**Workflow Procedures Include**:
- **Step 1.3**: One class of stock verification
  - Distribution pro-rata test with calculation
  - Debt vs equity factor analysis (maturity date, interest rate, payments, subordination)
  - Disproportionate distribution detection
- **Step 2.2**: AAA account step-by-step calculation
  - Beginning + income (ordinary + separately stated) - distributions (limited to AAA) - losses = ending
  - Critical rule: AAA can go negative from losses but NOT from distributions
  - Distribution ordering: AAA → PTI → E&P → Basis → Gain
- **Step 3**: Reasonable compensation analysis (MOST CRITICAL FOR S CORPS)
  - Multi-factor test with specific questions to ask
  - **Four calculation methodologies**:
    1. 60/40 rule (wages ≥ 40% of income)
    2. Market-based approach (BLS data for occupation + location)
    3. Employee comparison method
    4. Use highest result (most conservative)
  - Risk thresholds: ✓ OK (>50% of income), ⚠ Review (30-50%), 🔴 High Risk (<30%)
- **Step 4.1**: 2% shareholder health insurance exact treatment
  - Procedure: In W-2 Box 1 (YES), NOT in Boxes 3 & 5 (NO), S Corp deducts, shareholder claims Schedule 1
  - Step-by-step verification for each 2% shareholder
- **Step 6**: Shareholder basis tracking with proper ordering
  - Increases: income items + contributions
  - Decreases (in order): distributions → non-deductible expenses → depletion → losses
  - Basis cannot go negative; suspend excess losses
- **Step 7**: Built-in gains tax calculation for former C Corps within 5-year recognition period
- **Pass/Fail criteria** and specific correction procedures for each step

---

### Step 3: Systematic Review Execution

Review the uploaded return systematically by following each workflow procedure:

**3.1 Document Analysis**
- Extract all numerical data from forms
- Identify all attached schedules and supporting forms
- Note any missing schedules or forms that should be present
- Review for mathematical accuracy

**3.2 Workflow Execution**
Execute each workflow procedure step-by-step and categorize results as:
- **✓ VERIFIED** - Procedure completed, item is correct and compliant (include supporting details)
- **⚠ NEEDS REVIEW** - Procedure revealed issue requiring revision (specify what's wrong and how to fix)
- **? UNABLE TO VERIFY** - Insufficient information in uploaded document to complete procedure
- **N/A** - Procedure not applicable to this return

Follow the explicit instructions in each workflow step:
- Perform calculations shown in procedures
- Apply decision trees and if-then logic
- Use provided formulas and verification methods
- Test against Pass/Fail criteria stated in workflow

**3.3 Cross-References & Tie-Outs**
- Verify numbers tie between related schedules
- Check prior year carryforwards if comparable data available
- Confirm totals and subtotals are mathematically correct
- Validate percentages sum to 100% where required

**3.4 High-Risk Area Deep Dive**
Execute specialized workflow procedures for common error-prone areas:
- **1040**: 
  - K-1 box-by-box placement procedure (Step 2.5 in workflow)
  - Passive activity loss decision tree workflow
  - NIIT calculation procedure: threshold test → identify NII → calculate 3.8% tax
  - AMT requirement triggers and verification
- **1065**: 
  - Schedule M-2 capital flow verification (beginning → +contributions → +income → -distributions → -losses → ending = Schedule L)
  - K-1 summation procedure (sum all K-1s for each box must = Schedule K)
  - Liability allocation workflow (classify recourse vs nonrecourse, apply allocation rules)
- **1120S**: 
  - Reasonable compensation calculation (apply all 4 methodologies, use highest)
  - AAA account step-by-step (can go negative from losses only, not distributions)
  - 2% shareholder health insurance verification (W-2 Box 1 yes, Boxes 3&5 no)

---

### Step 4: Generate Review Report

Provide a comprehensive review report based on workflow execution results in the following format:

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

## DETAILED WORKFLOW RESULTS

### Step 1: Initial Data Verification
**Procedure 1.1 - Taxpayer Identification:**
- ✓ VERIFIED: Name "John Smith" present on Form 1040
- ✓ VERIFIED: SSN format correct (XXX-XX-1234), matches prior year
- ✓ VERIFIED: Address ties to prior year return

**Procedure 1.2 - Filing Status:**
- ✓ VERIFIED: Married Filing Jointly selected, both spouses present
- ✓ VERIFIED: Both taxpayer and spouse signatures obtained

**Procedure 1.3 - Dependent Information:**
- ✓ VERIFIED: Child #1 (Age 8) - SSN present, relationship verified, CTC checkbox correct
- ⚠ NEEDS REVIEW: Child #2 (Age 14) - SSN missing
  **Procedure Failed:** Step 1.3, item 2 - "Valid SSN present"
  **Location:** Form 1040, Dependents section, Child #2
  **Impact:** Cannot claim Child Tax Credit ($2,000), cannot e-file return
  **Action:** Obtain SSN for Child #2, update return before filing

### Step 2: Income Verification  
**Procedure 2.1 - W-2 Reconciliation:**
- ✓ VERIFIED: W-2 #1 Box 1 ($85,000) + W-2 #2 Box 1 ($0) = Form 1040 Line 1 ($85,000)
- ✓ VERIFIED: Federal withholding (Box 2: $12,500) = Form 1040 Line 25a

**Procedure 2.2 - Interest & Dividend Income:**
- ⚠ NEEDS REVIEW: Schedule B required but not filed
  **Procedure:** Step 2.2 - "Is taxable interest OR ordinary dividends > $1,500?"
  **Test Result:** Interest income $2,100 > $1,500 threshold
  **Current:** No Schedule B attached
  **Should Be:** Schedule B with all sources listed, totaling $2,100
  **Action:** Complete Schedule B Part I, list all interest sources, total must equal Form 1040 Line 2b

**Procedure 2.3 - Schedule C Business Income:**
- ✓ VERIFIED: Gross receipts $45,000, expenses $0, net profit $45,000
- ⚠ NEEDS REVIEW: Schedule SE missing
  **Procedure:** Step 2.3 - "Is Schedule C net profit > $400?"
  **Test Result:** Net profit $45,000 > $400 threshold
  **Calculation:**
    - Schedule C Line 31: $45,000
    - × 92.35%: $41,558
    - × 15.3%: $6,358 self-employment tax
  **Current:** No Schedule SE filed
  **Impact:** $6,358 understatement of tax liability
  **Priority:** CRITICAL
  **Action:** Complete Schedule SE, flow Line 6 ($6,358) to Schedule 2 Line 4

[Continue for all workflow steps...]

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

Loading Form 1040 workflow procedures (9 steps)...
Executing Step 1: Initial Data Verification (4 procedures)...
Executing Step 2: Income Verification (6 procedures)...
  → Procedure 2.1: W-2 Reconciliation - ✓ VERIFIED
  → Procedure 2.2: Interest/Dividends - ⚠ ISSUE: Schedule B required ($2,100 > $1,500)
  → Procedure 2.3: Schedule C - ⚠ ISSUE: Schedule SE missing
      Calculation: $45,000 × 92.35% × 15.3% = $6,358 SE tax
[... continues through all 9 steps ...]

Workflow Execution Complete.

Summary: 8 issues identified requiring revision
- 3 Critical (must fix before filing)
  1. Schedule SE missing - $6,358 tax understatement
  2. NIIT not calculated - $950 tax understatement  
  3. Schedule B required - compliance violation
- 3 Compliance (should fix)
- 2 Optimization opportunities

Most significant issue: 
**Procedure 2.3 - Schedule C SE Tax**
  Test: "Is Schedule C net profit > $400?"
  Result: $45,000 > $400 ✓ Yes
  Required: Schedule SE
  Current: Missing
  Calculation: $45,000 × 92.35% × 15.3% = $6,358
  Impact: $6,358 understatement of self-employment tax
  Action: Complete Schedule SE, flow Line 6 to Schedule 2 Line 4
```

---

## How to Use Workflow Procedures

### Understanding the Workflow Format

Each workflow consists of **numbered steps** with **explicit procedures**:

```markdown
### Step 2.1: W-2 Reconciliation (Line 1)
**Procedure:**
1. Locate Line 1 on Form 1040
2. Count number of W-2s 
3. For EACH W-2, extract Box 1
4. Sum all W-2 Box 1 amounts
5. Verify sum equals Line 1

**Mathematical Check:**
W-2 #1 Box 1: $______
W-2 #2 Box 1: $______
TOTAL: $______ ← Must equal Form 1040 Line 1

**Pass Criteria:** All W-2s accounted for, sum equals Line 1
**Fail Criteria:** Missing W-2s, math error, mismatch
```

**Execute each procedure exactly as written**, following the numbered steps and applying the verification tests.

### Integration with Workflow

#### Optimal Usage Pattern
1. **Initial Review**: Upload return, let skill execute all workflow procedures
2. **Review Findings**: Examine detailed workflow results with specific procedures that passed/failed
3. **Focused Verification**: Senior reviewer verifies flagged procedures and applies judgment
4. **Corrections**: Make corrections following the specific "Action" instructions provided
5. **Final Verification**: Re-run skill to confirm all procedures now pass

#### Time Savings
- **Manual workflow review**: 45-60 minutes (following procedures manually)
- **AI workflow execution**: 2-3 minutes (procedures executed automatically)
- **Result**: Senior reviewer focuses on judgment calls, complex fact patterns, and planning, not mechanical procedure execution

#### Training Tool
- **Teach procedures**: Use workflow outputs to show junior staff HOW to perform each verification
- **Learn from errors**: Each finding shows the procedure, test applied, and why it failed
- **Build expertise**: Workflows serve as instructional guides for learning tax return review

---

## Continuous Improvement

The workflow procedures should be updated annually for:
- **Tax law changes**: Update procedures to reflect new laws, thresholds, rates
- **New form revisions**: Modify procedures for form line number changes
- **Emerging IRS audit focus areas**: Add procedures for newly problematic areas
- **Firm-specific error patterns**: Customize workflows based on common firm errors discovered
- **State tax law updates**: Update state-specific procedures and thresholds
- **Procedure refinements**: Improve clarity and effectiveness of specific verification steps based on usage

---

## Limitations & Disclaimers

**This skill provides**:
- **Systematic workflow-based review** with explicit step-by-step procedures
- **Mechanical verification** of calculations, tie-outs, and compliance requirements
- **Common error detection** using proven testing procedures
- **Procedural guidance** showing HOW to perform each verification
- **Planning opportunity identification** based on workflow findings

**This skill does NOT replace**:
- **Professional judgment** on complex fact patterns or gray areas
- **Client-specific analysis** requiring knowledge of client circumstances beyond the return
- **Complex tax research** on unusual or novel issues
- **Legal or audit representation**
- **Business advisory services**

**How to Use**: The workflows execute mechanical review procedures. Professional judgment is still required for:
- Evaluating reasonableness of items beyond mathematical verification
- Determining appropriate treatment for unusual transactions
- Applying facts and circumstances tests
- Making elections and strategic planning decisions

**Professional responsibility remains with the reviewing CPA.** Workflows are tools to ensure mechanical procedures are performed correctly and consistently.

---

## Technical Notes

### Form Detection Algorithm
1. Parse PDF text content
2. Search for form identifiers in headers
3. Verify with secondary indicators (schedules, terminology)
4. Extract tax year and entity information

### Workflow Execution
1. Load appropriate guideline workflow file (1040.md, 1065.md, or 1120S.md)
2. Parse workflow structure (Steps → Procedures → Verification tests)
3. Execute each procedure sequentially:
   - Follow numbered procedural steps
   - Apply decision trees and if-then logic
   - Perform calculations per formulas provided
   - Test results against Pass/Fail criteria
4. Categorize results (✓ verified / ⚠ needs review / ? unable to verify / N/A)
5. Generate formatted output with:
   - Procedure identification (Step X.Y)
   - Test performed and result
   - Specific findings with calculations
   - Action items for corrections

### Quality Assurance
- Cross-reference multiple data points for verification
- Flag inconsistencies automatically
- Provide confidence level for each finding
- Note any limitations in document analysis

