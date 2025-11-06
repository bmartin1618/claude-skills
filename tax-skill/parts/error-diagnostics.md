# Tax Return Error Diagnostic Tool

## High-Frequency Errors in Complex Returns

### Partnership Return (1065) Diagnostics

#### Capital Account Errors
**Symptom**: Schedule K-1 capital accounts don't tie to Schedule L
**Check Points**:
- [ ] Verify beginning balances match prior year ending
- [ ] Check if using tax basis vs GAAP vs 704(b)
- [ ] Ensure all partners' capital accounts foot to total
- [ ] Verify distributions recorded in correct period
- [ ] Check for improper adjustment for tax-exempt income

**Quick Fix Formula**:
```
Beginning Capital (all partners) 
+ Contributions
+ Income Allocations
- Loss Allocations
- Distributions
= Ending Capital (must equal Schedule L equity)
```

#### Passive Activity Misclassification
**Symptom**: Incorrect passive/non-passive designation
**Check Points**:
- [ ] Limited partners automatically passive (unless exception)
- [ ] General partners - verify material participation tests
- [ ] Self-rental rules properly applied
- [ ] Grouping elections documented and consistent
- [ ] Real estate professional status analyzed

**Material Participation Quick Test**:
1. 500+ hours? → Non-passive
2. Substantially all participation? → Non-passive
3. 100+ hours and no one does more? → Non-passive
4. Aggregated significant participation >500? → Non-passive
5. Material participation 5 of last 10 years? → Non-passive

#### Liability Allocation Errors
**Symptom**: K-1 liability allocations don't match partnership total
**Check Points**:
- [ ] Recourse debt traced to obligated partners
- [ ] Nonrecourse debt allocated per profit ratios
- [ ] Qualified nonrecourse financing rules applied
- [ ] Partner guarantees increase recourse share
- [ ] DROs (deficit restoration obligations) considered

### S Corporation (1120S) Diagnostics

#### Reasonable Compensation Issues
**Symptom**: Officer compensation suspiciously low
**Red Flags**:
- Profitable S Corp with <$50k officer wages
- Distributions exceed wages significantly
- Officer works full-time but minimal/no wages
- Wages just below Social Security cap

**Safe Harbor Analysis**:
```
Industry Average Salary: $________
Company Net Income: $________
Officer Hours Worked: ________
Suggested Minimum: Greater of $50k or 40% of profits
```

#### AAA Account Errors
**Symptom**: Distributions exceed AAA causing unexpected tax
**Check Points**:
- [ ] Beginning AAA from prior return
- [ ] Add: Ordinary income (not tax-exempt)
- [ ] Add: Separately stated income items
- [ ] Subtract: Distributions (limited to AAA)
- [ ] Subtract: Losses and deductions
- [ ] Verify no negative AAA

**Distribution Ordering**:
1. AAA (tax-free to extent of basis)
2. PTI (if pre-1983 S Corp)
3. E&P (taxable dividend)
4. Return of basis (tax-free)
5. Excess (capital gain)

#### Basis Limitation Mistakes
**Symptom**: Losses claimed exceed shareholder basis
**Check Points**:
- [ ] Stock basis calculated correctly
- [ ] Debt basis only from direct loans
- [ ] Distributions reduce stock basis first
- [ ] Losses reduce stock basis before debt
- [ ] Restoration of debt basis rules

**Loss Allowance Order**:
1. Use stock basis first
2. Then use debt basis
3. Suspend excess losses

### Individual Return (1040) Diagnostics

#### K-1 Flow-Through Errors
**Symptom**: K-1 items missing or misplaced on 1040
**Common Mistakes**:
- Box 1 ordinary income → Schedule E, not Schedule C
- Box 5 interest → Schedule B (even if <$1,500)
- Box 9a LTCG → Schedule D, not just line item
- Box 11 other income → check code for placement
- Box 13 items → various locations per code
- Box 20 items → check state modification needs

#### Net Investment Income Tax (NIIT) Misses
**Symptom**: NIIT not calculated when required
**Quick Check**:
```
MAGI > $200k (single) or $250k (MFJ)?
  If yes → Check for investment income:
    - Interest, dividends, capital gains
    - Passive activity income
    - Rental income
    - Royalties
  Calculate: 3.8% × lesser of:
    - Net investment income, or
    - MAGI excess over threshold
```

#### Passive Loss Traps
**Symptom**: Suspended losses not properly tracked
**Verification Steps**:
- [ ] Prior year suspended losses carried forward
- [ ] Current year passive income identified
- [ ] Losses released up to passive income
- [ ] Remaining losses suspended
- [ ] Full disposition triggers all suspended losses

### Multi-State Filing Errors

#### Nexus Oversights
**Symptom**: Missing state filing requirements
**Quick Nexus Check**:
- Physical presence (office, employees, property)
- Economic nexus (usually $100k-500k sales)
- Factor presence (property, payroll, sales thresholds)
- Affiliate nexus
- Click-through nexus

#### Apportionment Errors
**Common Mistakes**:
- Using cost-of-performance vs market-based
- Including/excluding throwback sales incorrectly
- Non-business income allocation errors
- Special industry apportionment missed
- Combined reporting adjustments

**Basic Three-Factor Formula**:
```
(State Sales/Total Sales × Sales Weight) +
(State Payroll/Total Payroll × Payroll Weight) +
(State Property/Total Property × Property Weight) 
= Apportionment Percentage
```

## Quick Error Detection Ratios

### Red Flag Ratios That Suggest Errors

#### Effective Tax Rate Analysis
```
Federal Effective Rate = Tax ÷ Taxable Income
Expected Range: 10-37% (individuals), 21% (C corps)
If outside range → Review calculation
```

#### Profit Margin Concerns
```
Gross Profit Margin = (Revenue - COGS) ÷ Revenue
If <20% → Verify COGS calculation
If >80% → Check revenue recognition
```

#### Expense Ratios
```
Officer Comp ÷ Net Income <25% → Too low?
Interest ÷ Revenue >10% → Related party?
Meals ÷ Revenue >3% → Documentation?
```

## Automation Opportunities

### Excel Formulas for Common Checks

#### Tie Out Schedule L to M-2
```excel
=IF(L_Equity_End=M2_Capital_End,"TIES","CHECK")
```

#### K-1 Capital Account Verification
```excel
=SUMIF(Partner_Column,Partner_Name,Capital_End)
```

#### Basis Limitation Test
```excel
=MIN(Loss_Amount,Available_Basis)
```

#### State Apportionment Validation
```excel
=SUM(State_Percentages)  // Should equal 100%
```

## Software Diagnostic Priorities

### Must Fix (Return Won't File)
1. Missing required information
2. Mathematical errors
3. Social Security number issues
4. Dependent conflicts
5. Filing status problems

### Should Fix (Likely Errors)
1. Large year-over-year changes
2. Missing carryforwards
3. Diagnostic overrides without documentation
4. Round numbers suggesting estimates
5. Missing state returns

### Consider Fixing (Optimization)
1. Missed elections
2. Suboptimal depreciation methods
3. Credit vs deduction choices
4. Extension payment suggestions
5. Estimated tax recommendations

## Review Time Allocation Guide

### Suggested Time per Return Type
- **Simple 1040** (W-2, standard): 15-20 minutes
- **Complex 1040** (K-1s, rentals): 30-45 minutes
- **1065 Partnership**: 45-75 minutes
- **1120S S Corp**: 40-60 minutes
- **Multi-state returns**: Add 10-15 minutes per state

### Time Distribution
- 30% - Income verification
- 25% - Deduction/credit review
- 20% - Tax calculation check
- 15% - State return coordination
- 10% - Planning opportunities

## Critical Date Reminders

### Filing Deadlines (Without Extension)
- **1065**: March 15
- **1120S**: March 15
- **1040**: April 15

### Extension Deadlines
- **1065**: September 15
- **1120S**: September 15
- **1040**: October 15

### Key Compliance Dates
- **1099s**: January 31 to recipients, February 28 to IRS
- **W-2s**: January 31 to both
- **K-1s**: Should issue by entity due date
- **Estimates**: 4/15, 6/15, 9/15, 1/15

## Documentation Standards

### Minimum Workpaper Requirements
- [ ] Tax return checklist completed
- [ ] Tie-out of all source documents
- [ ] Prior year comparison
- [ ] Carryforward schedule
- [ ] Tax planning memo
- [ ] Review notes cleared
- [ ] Open items list
- [ ] Representation letter (if needed)

### Best Practice File Structure
```
ClientName_2024/
├── Source_Documents/
│   ├── W2_1099s/
│   ├── K1s/
│   └── Receipts/
├── Workpapers/
│   ├── Federal/
│   ├── States/
│   └── Calculations/
├── Correspondence/
├── Filed_Returns/
└── Planning_Memos/
```