# Multiple K-1 Tracking Excel Workbook

## Workbook Structure
Create an Excel file with these 7 tabs:

---

## Tab 1: K-1 Master Dashboard

```excel
=== K-1 MASTER DASHBOARD ===

A1: TAX YEAR: [2024]
A2: TAXPAYER: [Name]
A3: PREPARED BY: [Initials]
A4: DATE: [=TODAY()]

=== K-1 SUMMARY TABLE ===
A6: Entity Name
B6: EIN
C6: Entity Type
D6: Box 1 Income/(Loss)
E6: Self-Rental?
F6: Material Part?
G6: Character
H6: QBI Amount
I6: Basis Status
J6: State Issues
K6: Review Notes

[Rows 7-25 for data entry]

A27: TOTALS
D27: =SUM(D7:D25)
H27: =SUM(H7:H25)

=== PASSIVE ACTIVITY SUMMARY ===
A30: Activity Type
B30: Income
C30: Loss
D30: Net

A31: Non-Passive Activities
B31: =SUMIF(G7:G25,"Non-Passive",D7:D25)
C31: =SUMIF(G7:G25,"Non-Passive",D7:D25)
D31: =B31+C31

A32: Passive Activities
B32: =SUMIF(G7:G25,"Passive",D7:D25)*(D7:D25>0)
C32: =SUMIF(G7:G25,"Passive",D7:D25)*(D7:D25<0)
D32: =B32+C32

A33: Self-Rental Recharacterized
B33: [Formula for recharacterized income]
C33: [Stays as passive if loss]
D33: =B33+C33

=== QBI SUMMARY ===
A36: QBI Category
B36: Amount
C36: W-2 Wages
D36: UBIA
E36: Limitation

A37: Total QBI Income
B37: =SUMIF(H7:H25,">0",H7:H25)

A38: Total QBI Loss
B38: =SUMIF(H7:H25,"<0",H7:H25)

A39: Net QBI
B39: =B37+B38

=== KEY METRICS ===
A42: Check Item
B42: Status
C42: Action Required

A43: Basis Limitations Exist?
B43: =IF(COUNTIF(I7:I25,"Limited")>0,"YES","No")
C43: =IF(B43="YES","See Basis Tab","OK")

A44: Self-Rental Issues?
B44: =IF(COUNTIF(E7:E25,"Yes")>0,"YES","No")
C44: =IF(B44="YES","Review Recharacterization","OK")

A45: Passive Losses Suspended?
B45: =IF(D32<0,"YES","No")
C45: =IF(B45="YES","Track Carryforward","OK")

A46: QBI Aggregation Possible?
B46: =IF(COUNTIF(H7:H25,"<>0")>1,"Check","N/A")
C46: =IF(B46="Check","See QBI Tab","OK")
```

---

## Tab 2: Basis Tracking

```excel
=== BASIS TRACKING BY ENTITY ===

A1: Entity
B1: Beginning Basis
C1: Contributions
D1: Share of Income
E1: Tax-Exempt Income
F1: Distributions
G1: Share of Losses
H1: Nondeductible Exp
I1: Debt Increase
J1: Debt Decrease
K1: Ending Basis
L1: At-Risk Amount
M1: Allowed Loss
N1: Suspended Loss

[Row 2-20 for each entity]

=== FORMULAS ===
K2: =B2+C2+D2+E2-F2+I2-J2-H2+MIN(0,MAX(G2,-(B2+C2+D2+E2-F2+I2-J2-H2)))
L2: =K2-[Nonrecourse debt adjustment]
M2: =MAX(G2,-K2)
N2: =G2-M2

=== MULTI-TIER BASIS ===
A25: Upper Tier Entity
B25: Lower Tier Entity
C25: Lower Tier K-1 Loss
D25: Upper Tier Basis Available
E25: Loss Allowed at Upper
F25: Suspended at Upper

=== STATE BASIS ADJUSTMENTS ===
A35: Entity
B35: Federal Basis
C35: Ohio Adjustment
D35: Ohio Basis
E35: Indiana Adjustment
F35: Indiana Basis
G35: Kentucky Adjustment
H35: Kentucky Basis

[Formulas for state adjustments based on bonus depreciation, etc.]

=== DEBT BASIS (S CORPS ONLY) ===
A45: S Corporation
B45: Stock Basis
C45: Direct Loans
D45: Total Basis
E45: Loss Allowed
F45: Reduces Stock First
G45: Then Reduces Debt
H45: Ending Stock
I45: Ending Debt
```

---

## Tab 3: Self-Rental Analysis

```excel
=== SELF-RENTAL RELATIONSHIP MAPPING ===

A1: Rental Entity
B1: Tenant Entity
C1: Rental Income/(Loss)
D1: Material Part in Tenant?
E1: Original Character
F1: Recharacterized As
G1: Tax Impact

[Rows 2-10 for relationships]

=== RECHARACTERIZATION RULES ===
F2: =IF(AND(C2>0,D2="Yes"),"Non-Passive",IF(C2<0,"Passive",E2))
G2: =IF(F2<>E2,"RECHARACTERIZED","No Change")

=== GROUPING ELECTION ANALYSIS ===
A15: Potential Grouping
B15: Rental Entity
C15: Operating Entity
D15: Same Business?
E15: Common Control?
F15: Geographic?
G15: Interdependent?
H15: Eligible?
I15: Benefit?

H16: =IF(COUNTIF(D16:G16,"Yes")>=2,"YES","No")
I16: =IF(AND(H16="Yes",[rental loss],[operating income]),"Unlock Losses","No Benefit")

=== IMPACT SUMMARY ===
A25: Scenario
B25: Without Recharacterization
C25: With Recharacterization
D25: Tax Difference

A26: Total Passive Income
B26: [Sum of passive before reclass]
C26: [Sum of passive after reclass]
D26: =(C26-B26)*[Tax Rate]

A27: Total Non-Passive
B27: [Sum before]
C27: [Sum after]
D27: =(C27-B27)*[Tax Rate]

A28: PAL Suspended
B28: [Calculate suspended]
C28: [Recalculate with reclass]
D28: =B28-C28

=== DOCUMENTATION CHECKLIST ===
A35: Required Documentation
B35: Status
C35: Location

A36: Lease Agreement
B36: [Yes/No]
C36: [File location]

A37: Ownership Percentages
A38: Material Participation Proof
A39: Rent at Fair Market Value?
A40: Business Purpose Documented?
```

---

## Tab 4: Passive Activity Tracking

```excel
=== MATERIAL PARTICIPATION TESTS ===

A1: Entity Name
B1: Test 1 (500hr)
C1: Test 2 (All)
D1: Test 3 (>100)
E1: Test 4 (Sig)
F1: Test 5 (5/10)
G1: Test 6 (Personal)
H1: Test 7 (Facts)
I1: Material Part?
J1: Character

[Rows 2-15 for entities]

I2: =IF(OR(B2="Pass",C2="Pass",D2="Pass",E2="Pass",F2="Pass",G2="Pass",H2="Pass"),"YES","NO")
J2: =IF(I2="YES","Non-Passive","Passive")

=== HOUR TRACKING ===
A20: Entity
B20: Jan
C20: Feb
D20: Mar
E20: Apr
F20: May
G20: Jun
H20: Jul
I20: Aug
J20: Sep
K20: Oct
L20: Nov
M20: Dec
N20: Total Hours
O20: Test Met?

N21: =SUM(B21:M21)
O21: =IF(N21>=500,"Test 1",IF(N21>=100,"Check Test 3","No"))

=== PASSIVE INCOME/LOSS MATCHING ===
A35: Passive Income Sources
B35: Amount
C35: Available for Offset

A40: Passive Losses
B40: Current Year
C40: Prior Suspended
D40: Total Available
E40: Used Current Year
F40: Suspended to Next

E41: =MIN(D41,SUM(C36:C38))
F41: =D41-E41

=== DISPOSITION TRACKING ===
A50: Disposed Activity
B50: Date
C50: Suspended PAL
D50: Gain/(Loss) on Sale
E50: Ordinary Loss Allowed
F50: Capital Gain Reduced
```

---

## Tab 5: QBI Optimization

```excel
=== QBI ENTITY ANALYSIS ===

A1: Entity
B1: Trade/Business?
C1: SSTB?
D1: Box 20 QBI
E1: W-2 Wages
F1: UBIA Property
G1: Wage Limit (25%)
H1: Wage/Property Limit
I1: Applied Limit
J1: Final QBI

G2: =E2*0.25
H2: =(E2*0.25)+(F2*0.025)
I2: =IF([Taxable Income Test],MIN(D2,MAX(G2,H2)),D2)
J2: =MIN(D2,I2)

=== AGGREGATION ANALYSIS ===
A15: Group Name
B15: Entities Included
C15: Combined QBI
D15: Combined Wages
E15: Combined UBIA
F15: Limitation Before
G15: Limitation After
H15: Benefit

[Analyze different aggregation scenarios]

=== QBI LOSS CARRYFORWARD ===
A30: Entity
B30: 2021 Loss
C30: 2022 Loss
D30: 2023 Loss
E30: 2024 Loss
F30: Total Suspended
G30: 2024 Income
H30: Released
I30: Remaining

H31: =MIN(F31,MAX(0,G31))
I31: =F31-H31

=== TAXABLE INCOME LIMITATION ===
A40: Taxable Income Before QBI
B40: 20% Limitation
C40: Total QBI Calculated
D40: Limited QBI Deduction
E40: Benefit Lost

B40: =A40*0.2
D40: =MIN(C40,B40)
E40: =MAX(0,C40-D40)

=== OPTIMIZATION STRATEGIES ===
A50: Strategy
B50: Current QBI
C50: Optimized QBI
D50: Tax Savings

A51: Aggregate All Eligible
A52: Separate SSTB
A53: Increase W-2 Wages
A54: Accelerate Income
```

---

## Tab 6: State Modifications

```excel
=== STATE K-1 ADJUSTMENTS ===

A1: Entity
B1: Federal Box 1
C1: OH Bonus Add
D1: OH Modified
E1: IN Adjustment
F1: IN Modified
G1: KY Adjustment
H1: KY Modified

=== OHIO MODIFICATIONS ===
C2: =B2*[168(k) adjustment factor]
D2: =B2+C2

=== INDIANA MODIFICATIONS ===
E2: =[Throwback adjustment if applicable]
F2: =B2+E2

=== KENTUCKY MODIFICATIONS ===
G2: =[LLET paid adjustment]
H2: =B2-G2

=== MULTI-STATE APPORTIONMENT ===
A15: Entity
B15: Total Income
C15: OH %
D15: OH Income
E15: IN %
F15: IN Income
G15: KY %
H15: KY Income

=== STATE FILING REQUIREMENTS ===
A30: Entity
B30: OH Nexus?
C30: OH Filing?
D30: IN Nexus?
E30: IN Filing?
F30: KY Nexus?
G30: KY Filing?
H30: Composite?

=== PTE TAX ELECTIONS ===
A40: Entity
B40: OH PET Elected?
C40: OH PET Tax
D40: IN PTET Elected?
E40: IN PTET Tax
F40: KY PTE Elected?
G40: KY PTE Tax
H40: Total PTE Tax
I40: Federal Benefit

I41: =H41*[Federal Tax Rate]
```

---

## Tab 7: Review & Documentation

```excel
=== REVIEW CHECKLIST ===

A1: Review Item
B1: Status
C1: Notes
D1: Workpaper Ref

A2: All K-1s Received?
A3: Basis Calculations Complete?
A4: Self-Rental Analysis Done?
A5: Material Participation Documented?
A6: PAL Tracking Updated?
A7: QBI Optimization Reviewed?
A8: State Modifications Applied?
A9: PTE Elections Considered?
A10: Prior Suspensions Applied?
A11: Grouping Elections Consistent?

=== CARRYFORWARD TRACKING ===
A15: Type
B15: Entity
C15: Amount
D15: Year Generated
E15: Notes

A16: Basis Suspension
A17: At-Risk Suspension
A18: Passive Loss
A19: QBI Loss
A20: Capital Loss
A21: NOL

=== PLANNING NOTES ===
A30: Item
B30: Current Treatment
C30: Alternative
D30: Potential Savings

=== OPEN ITEMS ===
A40: Item
B40: Needed From
C40: Due Date
D40: Status

=== FINAL REVIEW SIGNOFF ===
A50: Review Step
B50: Completed By
C50: Date
D50: Time

A51: Initial K-1 Entry
A52: Basis Calculations
A53: Character Determination
A54: Loss Limitations
A55: QBI Calculation
A56: State Modifications
A57: Final Review
A58: Partner Approval
```
