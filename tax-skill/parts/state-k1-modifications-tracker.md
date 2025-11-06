# State-Specific K-1 Modifications Tracker

## Overview
This tracker handles the complex state adjustments required when K-1 income flows through to Ohio, Indiana, and Kentucky returns. Each state has unique modifications that affect basis, income recognition, and apportionment.

## Master State Modification Grid

### Part 1: Modification Types by State

| Modification Type | Ohio | Indiana | Kentucky | Federal Impact |
|------------------|------|---------|----------|----------------|
| **Depreciation Adjustments** |
| Bonus Depreciation (168(k)) | Add back 5/6 | Add back portion | No adjustment | Increases state income |
| Section 179 | Add back excess over $25k | Follow federal | Follow federal | Timing difference |
| Prior Year Recovery | Subtract 1/5 or 1/6 | Subtract if added | N/A | Reduces state income |
| **Income Modifications** |
| Municipal Bond Interest | Add if non-OH | Add if non-IN | Add if non-KY | Taxable at state |
| Federal Deductions | Add state taxes | Add state taxes | Add state taxes | No federal change |
| **Pass-Through Items** |
| PTE Tax Paid | Subtract if elected | Subtract if elected | Subtract if elected | Federal deduction |
| Composite Tax Paid | Credit | Credit | Credit | May affect basis |

### Part 2: K-1 Specific Adjustments

```
PARTNERSHIP (1065) K-1 MODIFICATIONS
=====================================

Box 1 - Ordinary Income/Loss
----------------------------
Federal Amount: $(100,000)

Ohio Adjustments:
+ Bonus depreciation add-back (5/6 of 168k):  $  30,000
+ Section 179 excess (over $25,000):          $  10,000
- Prior year bonus recovery (1/5):            $ (6,000)
- PTE tax (if elected):                       $ (5,000)
Ohio Modified Box 1:                          $ (71,000)

Indiana Adjustments:
+ Bonus depreciation add-back:                $  25,000
+ State tax add-back:                         $   2,000
- PTET (if elected):                          $ (4,900)
Indiana Modified Box 1:                       $ (77,900)

Kentucky Adjustments:
- LLET paid by entity:                        $ (1,750)
- PTE tax (if elected):                       $ (5,000)
Kentucky Modified Box 1:                      $(106,750)

S CORPORATION (1120S) K-1 MODIFICATIONS
========================================

Box 1 - Ordinary Income/Loss
----------------------------
Federal Amount: $150,000

Ohio Adjustments:
+ Bonus depreciation add-back:                $  20,000
+ Related party expense add-back:             $   5,000
- Ohio PTE tax:                               $ (8,750)
Ohio Modified Box 1:                          $ 166,250

Indiana Adjustments:
+ Bonus depreciation add-back:                $  18,000
- Indiana PTET:                               $ (7,350)
Indiana Modified Box 1:                       $ 160,650

Kentucky Adjustments:
+ Federal tax deduction add-back:             $   3,000
- Kentucky PTE tax:                           $ (7,500)
Kentucky Modified Box 1:                      $ 145,500
```

## State Basis Tracking Worksheet

### Federal vs State Basis Reconciliation

```
ENTITY: ABC Partnership, LLC
TAX YEAR: 2024

                        Federal    Ohio      Indiana   Kentucky
Beginning Basis         $100,000   $115,000  $108,000  $100,000
Adjustments:
+ Contributions          20,000     20,000    20,000    20,000
+ Income                 50,000     50,000    50,000    50,000
+ Depreciation adj.         -       8,000     6,000        0
- Distributions         (30,000)   (30,000)  (30,000)  (30,000)
- Losses               (40,000)   (32,000)  (35,000)  (40,000)
- State-specific adj.       -      (2,000)   (1,000)   (1,750)
Ending Basis           $100,000   $129,000  $118,000  $ 98,250

Suspended Losses:
- Due to basis              $0         $0        $0        $0
- Due to at-risk            $0         $0        $0        $0  
- Due to passive        $15,000    $15,000   $15,000   $15,000
```

## Apportionment Impact Tracker

### Multi-State K-1 Income Allocation

```
ENTITY: Multi-State Operating Partnership
TOTAL PARTNERSHIP INCOME: $500,000

Apportionment Factors:
                     Ohio      Indiana   Kentucky  Other     Total
Sales Factor         30%       25%       20%       25%       100%
Property Factor      35%       20%       25%       20%       100%
Payroll Factor       40%       15%       30%       15%       100%

Applied Formula:
Ohio (3-factor):     (30%×2 + 35% + 40%) ÷ 4 = 33.75%
Indiana (single):    25% (sales only)
Kentucky (single):   20% (sales only)

Income Allocation:
Federal K-1 Box 1:   $500,000
Ohio Share:          $168,750 (33.75%)
Indiana Share:       $125,000 (25%)
Kentucky Share:      $100,000 (20%)
Other States:        $106,250 (21.25%)

State Modifications Applied:
Ohio Modified:       $168,750 + $25,000 (depreciation) = $193,750
Indiana Modified:    $125,000 + $18,000 (depreciation) = $143,000
Kentucky Modified:   $100,000 - $2,000 (LLET) = $98,000
```

## Throwback Sales Analysis

### Indiana Throwback Impact

```
PARTNERSHIP SALES ANALYSIS
Total Sales: $10,000,000

Sales by Destination:
Indiana:             $2,000,000 (taxable in IN)
Ohio:                $3,000,000 (taxable in OH)
Kentucky:            $1,500,000 (taxable in KY)
Tennessee:           $1,000,000 (no nexus, no tax)
Florida:             $1,500,000 (no income tax)
Delaware:            $1,000,000 (no nexus, no tax)

Indiana Throwback Calculation:
Base Indiana Sales:  $2,000,000
+ Tennessee (throw): $1,000,000
+ Florida (throw):   $1,500,000  
+ Delaware (throw):  $1,000,000
Total IN Sales:      $5,500,000 (55% vs 20% without throwback)

Impact on K-1:
Original Box 1 Allocation to IN: $100,000
Adjusted for Throwback:           $275,000
Additional Indiana Tax:           $175,000 × 4.9% = $8,575
```

## PTE Tax Election Tracker

### Pass-Through Entity Tax Comparison

```
ENTITY: XYZ Operating LLC
TOTAL INCOME: $1,000,000
PARTNERS: 4 individuals, all participating

                    Without PTE    With PTE      Benefit
OHIO:
Entity Tax          $0            $50,000       $(50,000)
Partner Credit      $0            $50,000       $ 50,000
SALT Limit Impact   $(10,000)     $0           $ 10,000
Federal Benefit     $0            $11,000       $ 11,000
Net Benefit:                                    $ 21,000

INDIANA:
Entity Tax          $0            $49,000       $(49,000)
Partner Credit      $0            $49,000       $ 49,000
SALT Limit Impact   $(10,000)     $0           $ 10,000
Federal Benefit     $0            $10,780       $ 10,780
Net Benefit:                                    $ 20,780

KENTUCKY:
Entity Tax          $0            $50,000       $(50,000)
Partner Credit      $0            $50,000       $ 50,000
SALT Limit Impact   $(10,000)     $0           $ 10,000
Federal Benefit     $0            $11,000       $ 11,000
Net Benefit:                                    $ 21,000
Note: Requires 100% of partners to elect
```

## State Filing Requirement Matrix

### Nexus and Filing Triggers

```
K-1 FILING REQUIREMENT CHECKER
==============================

Entity Name: ________________
Check all that apply:

OHIO Requirements:
□ Gross receipts > $500,000 (CAT filing)
□ Property in OH > $50,000 (nexus)
□ Payroll in OH > $50,000 (nexus)
□ Sales in OH > $500,000 (nexus)
□ 25% of property, payroll, or sales in OH
→ If any checked: File Form IT-1140

INDIANA Requirements:
□ Gross income > $1,000 from IN
□ Any business activity in IN
□ Sales into IN > $100,000
□ 200+ transactions in IN
→ If any checked: File Form IT-65

KENTUCKY Requirements:
□ Doing business in KY
□ $3,000+ in KY gross receipts (LLET)
□ Gross profits or receipts in KY
□ Property or payroll in KY
→ If any checked: File Form 765 and pay LLET

COMPOSITE RETURN OPTIONS:
Ohio:     Available for nonresidents
Indiana:  Available at 4.9% rate
Kentucky: Available at highest rate
```

## Common State K-1 Errors and Fixes

### Error Detection Checklist

```
COMMON ERRORS BY STATE
======================

OHIO Errors:
✗ Forgetting 5/6 bonus depreciation add-back
  Fix: Add to Box 1, track for 5-year recovery
✗ Missing CAT tax for >$150k gross receipts
  Fix: File CAT return, pay 0.26% on excess over $1M
✗ Not electing PTE when beneficial
  Fix: Elect by 4/15, saves ~21% federal benefit

INDIANA Errors:
✗ Missing throwback sales
  Fix: Recalculate apportionment with throwback
✗ Wrong county tax rate
  Fix: Use taxpayer's county of residence on 1/1
✗ Not tracking basis separately
  Fix: Maintain separate federal/state basis schedules

KENTUCKY Errors:
✗ Missing LLET minimum tax
  Fix: Pay minimum $175 even with losses
✗ Wrong calculation method for LLET
  Fix: Use lesser of gross receipts or gross profits method
✗ PTE election not unanimous
  Fix: All partners must elect or none get benefit
```

## Excel Formulas for State Modifications

### Automation Formulas

```excel
=== OHIO MODIFICATIONS ===
Bonus Depreciation Add-back:
=IF(FederalDepreciation>0,FederalDepreciation*5/6,0)

Bonus Depreciation Recovery (Year 2-6):
=IF(YearsSinceAddback<=5,OriginalAddback/5,0)

PTE Tax Benefit:
=IF(PTEElected="Yes",FederalK1*0.05,0)

CAT Tax Check:
=IF(GrossReceipts>150000,"CAT Required","No CAT")

=== INDIANA MODIFICATIONS ===
Throwback Sales:
=SUMIF(StateTaxable,"No",SalesAmount)

Apportionment with Throwback:
=(IndianaSales+ThrowbackSales)/TotalSales

County Tax:
=VLOOKUP(County,CountyRateTable,2,FALSE)*IndianaIncome

=== KENTUCKY MODIFICATIONS ===
LLET Calculation:
=MAX(175,MIN(GrossReceipts*0.00095,GrossProfits*0.0075))

PTE Eligibility:
=IF(COUNTIF(PartnerElections,"Yes")=COUNTA(PartnerElections),"Eligible","Not Eligible")

Pension Exclusion Impact:
=MIN(31110,PensionIncome)
```

## Year-End Planning Strategies

### State-Specific Opportunities

```
DECEMBER PLANNING CHECKLIST
===========================

OHIO Strategies:
□ Accelerate federal depreciation (adds to OH income next year)
□ Elect PTE by extended due date
□ Review municipal tax estimates
□ Consider CAT grouping election

INDIANA Strategies:
□ Evaluate throwback impact on sales
□ Time sales to avoid throwback
□ Consider composite vs individual filing
□ Review county residence before 12/31

KENTUCKY Strategies:
□ Ensure unanimous PTE consent
□ Prepay LLET if beneficial
□ Maximize pension exclusion
□ Consider installment sales for rate optimization

MULTI-STATE Strategies:
□ Review nexus in each state
□ Optimize apportionment factors
□ Coordinate PTE elections
□ Plan asset locations
□ Time income/deduction recognition
```

## Documentation Requirements

### Required Support by State

```
DOCUMENTATION CHECKLIST
======================

For Each K-1 Maintain:

FEDERAL:
□ Original K-1
□ Entity tax return copy
□ Ownership percentage docs
□ Basis calculation

OHIO:
□ IT-1140 copy
□ CAT returns if applicable
□ PTE election form
□ Municipal tax returns
□ Depreciation adjustments schedule

INDIANA:
□ IT-65 copy
□ Apportionment workpapers
□ Throwback sales analysis
□ County determination docs
□ PTET election

KENTUCKY:
□ Form 765 copy
□ LLET calculation
□ PTE unanimous consent
□ Apportionment schedule
□ Local tax returns
```

This comprehensive tracking system will help you manage the complex state modifications required for each K-1, ensuring compliance and optimization across all three states.