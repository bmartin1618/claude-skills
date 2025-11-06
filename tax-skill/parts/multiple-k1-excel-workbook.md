# Multiple K-1 Tracking Excel Workbook

## Workbook Structure
Create an Excel file with these 7 tabs:

## Tab 1: K-1 Master Dashboard

```excel
=== K-1 MASTER DASHBOARD ===

A1: TAX YEAR: [Input Year]
A2: TAXPAYER: [Input Name]
A3: PREPARED BY: [Input]
A4: DATE: =TODAY()

=== K-1 SUMMARY GRID ===
A6: Entity Name
B6: EIN
C6: Entity Type
D6: Box 1 Income/(Loss)
E6: Self-Rental?
F6: Material Part?
G6: Passive Status
H6: QBI Amount
I6: Beginning Basis
J6: Current Basis
K6: At-Risk Amount
L6: Allowed Loss
M6: Suspended Loss
N6: Notes

Row 7-25: [Data entry rows]

=== SUMMARY TOTALS ===
A27: TOTALS
D27: =SUM(D7:D25)
H27: =SUM(H7:H25)
L27: =SUM(L7:L25)
M27: =SUM(M7:M25)

=== PASSIVE ACTIVITY SUMMARY ===
A30: Passive Income (current year):
B30: =SUMIF(G7:G25,"Passive",D7:D25)
A31: Passive Losses (current year):
B31: =SUMIF(G7:G25,"Passive",D7:D25)
A32: Prior Year Suspended PAL:
B32: [Input]
A33: PAL Released This Year:
B33: =MIN(ABS(B31),B30)
A34: PAL Suspended to Next Year:
B34: =B32+IF(B31<0,ABS(B31)-B33,0)

=== QBI SUMMARY ===
A37: Total QBI Income:
B37: =SUMIF(H7:H25,">0",H7:H25)
A38: Total QBI Loss:
B38: =SUMIF(H7:H25,"<0",H7:H25)
A39: Net QBI:
B39: =B37+B38
A40: QBI Deduction (simplified):
B40: =MIN(B39*0.2,TaxableIncome*0.2)

=== KEY FORMULAS ===
Cell G7 (Passive Status - drag down):
=IF(E7="Yes",IF(D7>0,"Non-Passive","Passive"),IF(F7="Yes","Non-Passive","Passive"))

Cell L7 (Allowed Loss - drag down):
=IF(D7>=0,D7,MAX(D7,-MIN(J7,K7)))

Cell M7 (Suspended Loss - drag down):
=IF(D7>=0,0,ABS(D7)-ABS(L7))
```

## Tab 2: Basis Tracking

```excel
=== INDIVIDUAL BASIS TRACKING ===

A1: SELECT ENTITY: [Dropdown from Master list]
B1: =VLOOKUP(A1,Master!A7:B25,2,FALSE) 'Shows EIN

=== BASIS CALCULATION ===
A4: BEGINNING BASIS
A5: Beginning Tax Basis:
B5: [Input or link to prior year]
A6: Beginning At-Risk Amount:
B6: [Input or link to prior year]

A8: INCREASES TO BASIS
A9: Capital Contributions:
B9: [Input]
A10: Share of Income (Box 1 if positive):
B10: =IF(VLOOKUP(A1,Master!A7:D25,4,FALSE)>0,VLOOKUP(A1,Master!A7:D25,4,FALSE),0)
A11: Tax-Exempt Income:
B11: [Input]
A12: Other Income Items:
B12: [Input]
A13: Share of Liabilities Increase:
B13: [Input]
A14: Total Increases:
B14: =SUM(B9:B13)

A16: DECREASES TO BASIS
A17: Distributions - Cash:
B17: [Input]
A18: Distributions - Property:
B18: [Input]
A19: Share of Loss (Box 1 if negative):
B19: =IF(VLOOKUP(A1,Master!A7:D25,4,FALSE)<0,ABS(VLOOKUP(A1,Master!A7:D25,4,FALSE)),0)
A20: Nondeductible Expenses:
B20: [Input]
A21: Other Deductions:
B21: [Input]
A22: Share of Liabilities Decrease:
B22: [Input]
A23: Total Decreases:
B23: =SUM(B17:B22)

A25: ENDING CALCULATIONS
A26: Calculated Ending Basis:
B26: =B5+B14-B23
A27: Ending Basis (>=0):
B27: =MAX(0,B26)
A28: Loss Limited by Basis:
B28: =IF(B26<0,ABS(B26),0)

A30: AT-RISK CALCULATION
A31: Beginning At-Risk:
B31: =B6
A32: At-Risk Increases:
B32: =B14-B13+[Input for Recourse Debt]
A33: At-Risk Decreases:
B33: =B23-B22
A34: Ending At-Risk:
B34: =MAX(0,B31+B32-B33)
A35: Additional Loss Limited by At-Risk:
B35: =MAX(0,B19-B27-B34)

=== MULTI-STATE BASIS ===
A38: STATE BASIS ADJUSTMENTS
A39: State
B39: Federal Basis
C39: Modifications
D39: State Basis

A40: Ohio
B40: =B27
C40: [Input bonus dep add-back]
D40: =B40+C40

A41: Indiana
B41: =B27
C41: [Input modifications]
D41: =B41+C41

A42: Kentucky
B42: =B27
C42: [Input modifications]
D42: =B42+C42
```

## Tab 3: Material Participation

```excel
=== MATERIAL PARTICIPATION TRACKING ===

A1: TAX YEAR: [Link to Master]

=== HOURS TRACKING BY ENTITY ===
A4: Entity Name
B4: Test 1 (500 hrs)
C4: Test 2 (Substantially All)
D4: Test 3 (>100 hrs & most)
E4: Test 4 (Significant)
F4: Test 5 (5 of 10 years)
G4: Test 6 (Personal Service)
H4: Test 7 (Facts & Circumstances)
I4: Material Participation?
J4: Documentation

Row 5-20: [Entity names from Master]

=== DETAILED HOURS LOG ===
A23: Entity
B23: Date/Period
C23: Activity Description
D23: Hours
E23: Evidence

[Rows for detailed logging]

=== TEST CALCULATIONS ===
Cell I5 (Material Participation - drag down):
=IF(OR(B5>=500,C5="Yes",D5="Yes",E5="Yes",F5="Yes",G5="Yes",H5="Yes"),"YES","NO")

=== SIGNIFICANT PARTICIPATION TEST ===
A40: Significant Participation Activities (100-500 hours each):
A41: Entity
B41: Hours
C41: Qualifies?

A42-50: [List entities]
B42-50: [Input hours]
C42-50: =IF(AND(B42>=100,B42<500),"Yes","No")

A52: Total Significant Participation Hours:
B52: =SUMIF(C42:C50,"Yes",B42:B50)
A53: Material Participation via Test 4?
B53: =IF(B52>500,"YES","NO")
```

## Tab 4: Self-Rental Analysis

```excel
=== SELF-RENTAL RELATIONSHIP MAPPING ===

A1: SELF-RENTAL ANALYZER

=== RELATIONSHIP GRID ===
A4: Rental Entity
B4: Tenant Entity
C4: Rent Paid
D4: Material Part in Tenant?
E4: Rental Income/(Loss)
F4: Original Character
G4: Recharacterized As
H4: Tax Impact

A5: [Input rental entity]
B5: [Input tenant entity]
C5: [Input rent amount]
D5: [Yes/No dropdown]
E5: [Input from K-1]
F5: =IF(E5>0,"Passive Income","Passive Loss")
G5: =IF(AND(D5="Yes",E5>0),"Non-Passive Income",F5)
H5: =IF(F5<>G5,"RECHARACTERIZED","No Change")

=== GROUPING ANALYSIS ===
A15: POTENTIAL GROUPING OPPORTUNITIES
A16: Rental Entity
B16: Operating Entity
C16: Common Control?
D16: Same Business?
E16: Geographic Proximity?
F16: Interdependent?
G16: Can Group?
H16: Benefit of Grouping

A17: [Input]
B17: [Input]
C17: [Yes/No]
D17: [Yes/No]
E17: [Yes/No]
F17: [Yes/No]
G17: =IF(AND(C17="Yes",OR(D17="Yes",E17="Yes",F17="Yes")),"ELIGIBLE","Not Eligible")
H17: [Describe benefit]

=== NET IMPACT CALCULATOR ===
A25: Entity
B25: Character Before
C25: Income/(Loss)
D25: Character After
E25: Passive Income
F25: Non-Passive Income
G25: Passive Loss
H25: Non-Passive Loss

[Calculate net positions after recharacterization]

=== FORMULA FOR RECHARACTERIZATION ===
Cell G5: =IF(AND(D5="Yes",E5>0),"Non-Passive Income",IF(E5>0,"Passive Income","Passive Loss"))
```

## Tab 5: QBI Calculator

```excel
=== QBI QUALIFICATION AND CALCULATION ===

A1: QBI ANALYZER FOR MULTIPLE K-1s

=== QBI QUALIFICATION MATRIX ===
A4: Entity
B4: Trade/Business?
C4: SSTB?
D4: Box 1 Amount
E4: QBI Amount
F4: W-2 Wages
G4: UBIA Property
H4: Income Limit
I4: Wage/Property Limit
J4: Final QBI

A5-20: [Entity names from Master]
B5-20: [Yes/No]
C5-20: [Yes/No]
D5-20: [Link to Master]
E5-20: [Input from K-1 Box 20 Code Z]
F5-20: [Input from K-1]
G5-20: [Input from K-1]

=== AGGREGATION ANALYSIS ===
A23: AGGREGATION GROUPS
A24: Group
B24: Entities
C24: Combined QBI
D24: Combined Wages
E24: Combined UBIA
F24: Wage Limit
G24: Property Limit
H24: Greater Limit

A25: Group 1
B25: [List entities]
C25: =SUMIF(AggregationGroup,1,QBIColumn)
D25: =SUMIF(AggregationGroup,1,WagesColumn)
E25: =SUMIF(AggregationGroup,1,UBIAColumn)
F25: =D25*0.5
G25: =D25*0.25+E25*0.025
H25: =MAX(F25,G25)

=== TAXABLE INCOME LIMITATION ===
A35: Taxable Income Before QBI:
B35: [Input]
A36: 20% of Taxable Income:
B36: =B35*0.2
A37: Total QBI (before limits):
B37: =SUM(E5:E20)
A38: Total QBI (after W-2/UBIA limits):
B38: [Calculated based on limits]
A39: Final QBI Deduction:
B39: =MIN(B36,B38)

=== FORMULAS ===
Cell H5 (Income Limit Test - drag down):
=IF(TaxableIncome<157500,E5*0.2,IF(TaxableIncome>207500,"Apply Limit","Phase-in"))

Cell I5 (Wage/Property Limit - drag down):
=MAX(F5*0.5,F5*0.25+G5*0.025)

Cell J5 (Final QBI - drag down):
=IF(H5="Apply Limit",MIN(E5*0.2,I5),E5*0.2)
```

## Tab 6: Loss Carryforward

```excel
=== SUSPENDED LOSS TRACKING ===

A1: LOSS CARRYFORWARD TRACKER

=== BY ENTITY AND TYPE ===
A4: Entity
B4: Year Generated
C4: Basis Suspended
D4: At-Risk Suspended
E4: Passive Suspended
F4: Released Current
G4: Remaining

[Track each entity's suspended losses by type and year]

=== RELEASE WATERFALL ===
A20: CURRENT YEAR LOSS RELEASE
A21: Entity
B21: Beginning Suspended
C21: Current Income
D21: Amount Released
E21: Ending Suspended

A22-35: [Entity list]
B22: [Prior suspended amount]
C22: [Current year income if passive]
D22: =MIN(B22,MAX(0,C22))
E22: =B22-D22

=== STATE CARRYFORWARDS ===
A40: STATE LOSS TRACKING
A41: Entity
B41: Federal Suspended
C41: Ohio Suspended
D41: Indiana Suspended
E41: Kentucky Suspended

[Track differences in state carryforwards]

=== ORDERING RULES ===
A50: LOSS APPLICATION ORDER
A51: 1. Current year ordinary losses (to extent of basis)
A52: 2. Prior suspended basis losses (when basis restored)
A53: 3. Prior suspended at-risk losses (when at-risk restored)
A54: 4. Prior suspended passive losses (when passive income)
A55: 5. Remaining losses suspended to future years
```

## Tab 7: Planning Opportunities

```excel
=== TAX PLANNING OPPORTUNITIES ===

A1: PLANNING CHECKLIST FOR MULTIPLE K-1s

=== IMMEDIATE OPPORTUNITIES ===
A4: Opportunity
B4: Entity Affected
C4: Potential Benefit
D4: Action Required
E4: Deadline

A5: Group rentals with operations
B5: [List entities]
C5: Convert $X passive loss to active
D5: File grouping election
E5: Due date of return

A6: Increase material participation
B6: [List entities]
C6: Convert passive to non-passive
D6: Document additional hours
E6: 12/31

A7: PTE tax elections
B7: [List eligible entities]
C7: Federal SALT deduction
D7: Make elections
E7: 3/15 or 4/15

=== YEAR-END STRATEGIES ===
A15: Strategy
B15: Implementation
C15: Estimated Tax Savings

A16: Time distributions to manage basis
B16: [Specific steps]
C16: [Dollar amount]

A17: Accelerate/defer income between entities
B17: [Specific steps]
C17: [Dollar amount]

=== QBI OPTIMIZATION ===
A25: QBI PLANNING STRATEGIES
A26: Strategy
B26: Current QBI
C26: After Strategy
D26: Additional Deduction

A27: Aggregate entities
B27: [Current separate QBI]
C27: [Combined QBI with wages]
D27: =[Calculated benefit]

A28: Increase W-2 wages
B28: [Current limitation]
C28: [New limitation]
D28: =[Additional QBI allowed]

=== FORMULA LIBRARY ===
Benefit of Grouping:
=IF(PassiveLoss<0,MIN(ABS(PassiveLoss),ActiveIncome)*TaxRate,0)

PTE Tax Benefit:
=(EntityIncome*StateRate)-MAX(0,(EntityIncome*StateRate-10000))*0.37)

QBI Optimization:
=MIN(QBIAmount*0.2,MAX(Wages*0.5,Wages*0.25+UBIA*0.025))
```