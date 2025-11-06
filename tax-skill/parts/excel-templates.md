# Excel Templates for Tax Calculations

## Template 1: Partnership Basis Tracker

```excel
=== PARTNERSHIP BASIS TRACKER ===

A1: Partner Name
B1: Tax Year
C1: Partnership Name

=== BEGINNING BASIS ===
A5: Beginning Basis
B5: [Input prior year ending basis]

=== CURRENT YEAR INCREASES ===
A7: INCREASES TO BASIS
A8: Ordinary Income (K-1 Box 1)
B8: [Input]
A9: Rental Income (K-1 Box 2) 
B9: [Input]
A10: Interest Income (K-1 Box 5)
B10: [Input]
A11: Dividends (K-1 Box 6a)
B11: [Input]
A12: Capital Gains (K-1 Boxes 8-9)
B12: [Input]
A13: Tax-Exempt Income
B13: [Input]
A14: Other Income
B14: [Input]
A15: Capital Contributions
B15: [Input]
A16: Increase in Liabilities
B16: [Input]
A17: TOTAL INCREASES
B17: =SUM(B8:B16)

=== CURRENT YEAR DECREASES ===
A19: DECREASES TO BASIS
A20: Cash Distributions
B20: [Input - enter as positive]
A21: Property Distributions (FMV)
B21: [Input - enter as positive]
A22: Decrease in Liabilities
B22: [Input - enter as positive]
A23: Nondeductible Expenses
B23: [Input - enter as positive]
A24: Ordinary Loss (K-1 Box 1)
B24: [Input - enter as positive]
A25: Rental Loss (K-1 Box 2)
B25: [Input - enter as positive]
A26: Capital Losses
B26: [Input - enter as positive]
A27: Section 179 Deduction
B27: [Input - enter as positive]
A28: Charitable Contributions
B28: [Input - enter as positive]
A29: Other Deductions
B29: [Input - enter as positive]
A30: TOTAL DECREASES
B30: =SUM(B20:B29)

=== BASIS LIMITATION CHECK ===
A32: Basis Before Losses
B32: =B5+B17-SUM(B20:B23)
A33: Total Loss Items
B33: =SUM(B24:B29)
A34: Maximum Deductible Loss
B34: =MIN(B32,B33)
A35: Suspended Losses
B35: =MAX(0,B33-B34)

=== ENDING BASIS ===
A37: Ending Tax Basis
B37: =MAX(0,B5+B17-SUM(B20:B23)-B34)

=== AT-RISK LIMITATION ===
A40: Tax Basis (from above)
B40: =B37
A41: Plus: Recourse Debt
B41: [Input]
A42: Plus: Qualified Nonrecourse
B42: [Input]
A43: Less: Protected Amounts
B43: [Input - as positive]
A44: At-Risk Amount
B44: =B40+B41+B42-B43

=== FORMULAS TO COPY ===
Cell B17: =SUM(B8:B16)
Cell B30: =SUM(B20:B29)
Cell B32: =B5+B17-SUM(B20:B23)
Cell B33: =SUM(B24:B29)
Cell B34: =MIN(B32,B33)
Cell B35: =MAX(0,B33-B34)
Cell B37: =MAX(0,B5+B17-SUM(B20:B23)-B34)
Cell B44: =B40+B41+B42-B43
```

## Template 2: Multi-State Apportionment Calculator

```excel
=== MULTI-STATE APPORTIONMENT ===

=== SALES FACTOR ===
A1: State
B1: Sales
C1: Throwback
D1: Net Sales
E1: % of Total

A2: Ohio
B2: [Input]
C2: [Input throwback]
D2: =B2+C2
E2: =D2/$D$10

A3: Indiana
B3: [Input]
C3: [Input throwback]
D3: =B3+C3
E3: =D3/$D$10

A4: Kentucky
B4: [Input]
C4: 0 (no throwback)
D4: =B4+C4
E4: =D4/$D$10

A5: Other States
B5: [Input]
C5: [Input]
D5: =B5+C5
E5: =D5/$D$10

A10: TOTAL
B10: =SUM(B2:B5)
C10: =SUM(C2:C5)
D10: =SUM(D2:D5)
E10: =SUM(E2:E5)

=== PROPERTY FACTOR (if applicable) ===
A12: State
B12: Property Value
C12: % of Total

A13: Ohio
B13: [Input]
C13: =B13/$B$17

A14: Indiana
B14: [Input]
C14: =B14/$B$17

A15: Kentucky
B15: [Input]
C15: =B15/$B$17

A17: TOTAL
B17: =SUM(B13:B15)
C17: =SUM(C13:C15)

=== PAYROLL FACTOR (if applicable) ===
A19: State
B19: Payroll
C19: % of Total

A20: Ohio
B20: [Input]
C20: =B20/$B$24

A21: Indiana
B21: [Input]
C21: =B21/$B$24

A22: Kentucky
B22: [Input]
C22: =B22/$B$24

A24: TOTAL
B24: =SUM(B20:B22)
C24: =SUM(C20:C22)

=== APPORTIONMENT SUMMARY ===
A26: State
B26: Method
C26: Sales %
D26: Property %
E26: Payroll %
F26: Apportionment %

A27: Ohio
B27: 3-Factor
C27: =E2*2
D27: =C13
E27: =C20
F27: =(C27+D27+E27)/4

A28: Indiana
B28: Single Sales
C28: =E3
D28: N/A
E28: N/A
F28: =C28

A29: Kentucky
B29: Single Sales
C29: =E4
D29: N/A
E29: N/A
F29: =C29

=== INCOME ALLOCATION ===
A32: Total Income
B32: [Input]

A34: State
B34: Apportionment %
C34: Allocated Income
D34: Tax Rate
E34: Tax

A35: Ohio
B35: =F27
C35: =$B$32*B35
D35: 0% (pass-through)
E35: =C35*D35

A36: Indiana  
B36: =F28
C36: =$B$32*B36
D36: 4.9%
E36: =C36*D36

A37: Kentucky
B37: =F29
C37: =$B$32*B37
D37: 5.0%
E37: =C37*D37

A39: TOTAL TAX
B39: =SUM(E35:E37)
```

## Template 3: S Corporation Reasonable Compensation Analysis

```excel
=== REASONABLE COMPENSATION ANALYSIS ===

=== COMPANY INFORMATION ===
A1: Company Name
B1: [Input]
A2: Tax Year
B2: [Input]
A3: Industry
B3: [Input]

=== FINANCIAL DATA ===
A5: Net Income (before officer comp)
B5: [Input]
A6: Distributions to Shareholders
B6: [Input]
A7: Current Officer Compensation
B7: [Input]

=== BENCHMARK ANALYSIS ===
A10: Compensation Method
B10: Amount
C10: Source

A11: Industry Average (Bureau of Labor)
B11: [Input]
C11: www.bls.gov

A12: RCReports.com Estimate
B12: [Input]
C12: RCReports

A13: 50% of Net Income Method
B13: =B5*0.5
C13: Rule of Thumb

A14: Social Security Max Base
B14: 168600
C14: 2024 Limit

A15: Distribution/Wage Ratio (Target 60/40)
B15: =B7/(B6+B7)
C15: IRS Guidance

=== REASONABLENESS TEST ===
A18: Test
B18: Current
C18: Pass/Fail
D18: Recommended

A19: Minimum Compensation Test
B19: =B7
C19: =IF(B19>=50000,"PASS","FAIL")
D19: =MAX(50000,B5*0.4)

A20: Industry Comparison
B20: =B7/B11
C20: =IF(B20>=0.7,"PASS","REVIEW")
D20: =B11*0.85

A21: Distribution Ratio Test
B21: =B6/B7
C21: =IF(B21<=1.5,"PASS","FAIL")
D21: Safe if < 1.5:1

A22: Profit Percentage Test
B22: =B7/B5
C22: =IF(B22>=0.4,"PASS","REVIEW")
D22: =B5*0.4

=== RECOMMENDED COMPENSATION ===
A25: Analysis Result
A26: Current Officer Compensation
B26: =B7
A27: Recommended Minimum
B27: =MAX(D19,D20,D22)
A28: Additional W-2 Wages Needed
B28: =MAX(0,B27-B26)

=== PAYROLL TAX IMPACT ===
A30: Additional Wages
B30: =B28
A31: Social Security (12.4%)
B31: =MIN(B30,168600-B7)*0.124
A32: Medicare (2.9%)
B32: =B30*0.029
A33: Additional Medicare (1.8%)
B33: =IF(B7+B30>200000,(B7+B30-200000)*0.018,0)
A34: Total Additional Tax
B34: =B31+B32+B33

=== FORMULAS ===
Cell B13: =B5*0.5
Cell B15: =B7/(B6+B7)
Cell C19: =IF(B19>=50000,"PASS","FAIL")
Cell D19: =MAX(50000,B5*0.4)
Cell C20: =IF(B20>=0.7,"PASS","REVIEW")
Cell D20: =B11*0.85
Cell B20: =B7/B11
Cell B21: =B6/B7
Cell C21: =IF(B21<=1.5,"PASS","FAIL")
Cell B22: =B7/B5
Cell C22: =IF(B22>=0.4,"PASS","REVIEW")
Cell D22: =B5*0.4
Cell B27: =MAX(D19,D20,D22)
Cell B28: =MAX(0,B27-B26)
Cell B31: =MIN(B30,168600-B7)*0.124
Cell B32: =B30*0.029
Cell B33: =IF(B7+B30>200000,(B7+B30-200000)*0.018,0)
Cell B34: =B31+B32+B33
```

## Template 4: Passive Activity Loss Tracker

```excel
=== PASSIVE ACTIVITY LOSS TRACKER ===

=== ACTIVITY INFORMATION ===
A1: Activity Name
B1: [Input]
A2: Activity Type
B2: [Rental/Trade/Business]
A3: Material Participation?
B3: [Yes/No]

=== CURRENT YEAR ===
A5: Current Year Income/(Loss)
B5: [Input]
A6: Current Year Passive Income
B6: [Input if passive]
A7: Current Year Passive Loss
B7: =IF(B3="No",MIN(0,B5),0)

=== CARRYFORWARD TRACKING ===
A10: Year
B10: Suspended Loss
C10: Released
D10: Remaining

A11: Prior Years Total
B11: [Input]
C11: 0
D11: =B11

A12: Current Year
B12: =ABS(B7)
C12: =MIN(D11+B12,MAX(0,B6))
D12: =D11+B12-C12

=== DISPOSITION CALCULATION ===
A15: Disposition This Year?
B15: [Yes/No]
A16: Sales Price
B16: [Input if yes]
A17: Adjusted Basis
B17: [Input if yes]
A18: Gain/(Loss) on Sale
B18: =IF(B15="Yes",B16-B17,0)
A19: Suspended Losses Released
B19: =IF(B15="Yes",D12,0)
A20: Total Loss on Disposition
B20: =B18-B19

=== MATERIAL PARTICIPATION TESTS ===
A23: Test Description
B23: Hours/Criteria
C23: Met?

A24: 1. 500 Hour Test
B24: [Input hours]
C24: =IF(B24>=500,"YES","NO")

A25: 2. Substantially All
B25: [Input %]
C25: =IF(B25>=90%,"YES","NO")

A26: 3. More than 100 hours, most
B26: [Input hours]
C26: [Manual Yes/No]

A27: 4. Significant Participation
B27: [Input total hours]
C27: =IF(B27>500,"YES","NO")

A28: 5. Prior 5 of 10 years
B28: [Input # years]
C28: =IF(B28>=5,"YES","NO")

A29: Material Participation Met?
B29: =IF(COUNTIF(C24:C28,"YES")>0,"YES","NO")

=== RENTAL REAL ESTATE PROFESSIONAL ===
A32: RE Professional Status?
B32: [Yes/No]
A33: Hours in RE Trade
B33: [Input]
A34: More than 50% of Time?
B34: =IF(B33>750,"Likely","Check")
A35: Each Property >100 hrs?
B35: [Yes/No]

=== FORMULAS ===
Cell B7: =IF(B3="No",MIN(0,B5),0)
Cell C12: =MIN(D11+B12,MAX(0,B6))
Cell D12: =D11+B12-C12
Cell B18: =IF(B15="Yes",B16-B17,0)
Cell B19: =IF(B15="Yes",D12,0)
Cell B20: =B18-B19
Cell C24: =IF(B24>=500,"YES","NO")
Cell C25: =IF(B25>=0.9,"YES","NO")
Cell C27: =IF(B27>500,"YES","NO")
Cell C28: =IF(B28>=5,"YES","NO")
Cell B29: =IF(COUNTIF(C24:C28,"YES")>0,"YES","NO")
Cell B34: =IF(B33>750,"Likely","Check")
```

## Template 5: State Tax Quick Calculator

```excel
=== TRI-STATE TAX CALCULATOR ===

=== INPUT DATA ===
A1: Taxable Income
B1: [Input]
A2: Entity Type
B2: [S Corp/Partnership/LLC]

=== OHIO CALCULATIONS ===
A5: OHIO
A6: CAT Gross Receipts
B6: [Input]
A7: CAT Tax (0.26% over $1M)
B7: =MAX(0,(B6-1000000)*0.0026)
A8: PET Election?
B8: [Yes/No]
A9: PET Tax (5%)
B9: =IF(B8="Yes",B1*0.05,0)
A10: Municipal Rate
B10: [Input %]
A11: Municipal Tax
B11: =B1*B10
A12: Total Ohio Tax
B12: =B7+B9+B11

=== INDIANA CALCULATIONS ===
A15: INDIANA
A16: Apportioned Income
B16: =B1*[Input %]
A17: State Tax (4.9%)
B17: =B16*0.049
A18: County Rate
B18: [Input %]
A19: County Tax
B19: =B16*B18
A20: PTET Election?
B20: [Yes/No]
A21: Total Indiana Tax
B21: =IF(B20="Yes",B16*0.049,B17+B19)

=== KENTUCKY CALCULATIONS ===
A24: KENTUCKY
A25: Apportioned Income
B25: =B1*[Input %]
A26: LLET Gross Receipts
B26: [Input]
A27: LLET Gross Profits
B27: [Input]
A28: LLET (lesser calculation)
B28: =MAX(175,MIN(B26*0.00095,B27*0.0075))
A29: PTE Election?
B29: [Yes/No]
A30: PTE/Income Tax (5%)
B30: =IF(B29="Yes",B25*0.05,0)
A31: Local Net Profit Rate
B31: [Input %]
A32: Local Tax
B32: =B25*B31
A33: Total Kentucky Tax
B33: =B28+B30+B32

=== SUMMARY ===
A36: STATE TAX SUMMARY
A37: State
B37: Entity Tax
C37: PTE Tax
D37: Local Tax
E37: Total

A38: Ohio
B38: =B7
C38: =B9
D38: =B11
E38: =B12

A39: Indiana
B39: 0
C39: =IF(B20="Yes",B21,0)
D39: =IF(B20="No",B19,0)
E39: =B21

A40: Kentucky
B40: =B28
C40: =B30
D40: =B32
E40: =B33

A42: TOTAL ALL STATES
B42: =SUM(E38:E40)

A44: Effective Rate
B44: =B42/B1
```