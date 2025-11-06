# Excel Templates for Tax Return Review
## Implementation Guide and Formulas

---

## WORKBOOK 1: Partnership Basis Tracker
**Filename**: Partnership_Basis_Tracker.xlsx

### Sheet 1: Partner Information
```excel
| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| Partner Name | Tax ID | % Ownership | Type | Profit % | Loss % | Capital % |
| =INPUT | =INPUT | =INPUT | =DROPDOWN | =INPUT | =INPUT | =INPUT |

DROPDOWN Formula for Column D:
={"Individual";"Corporation";"Partnership";"Trust";"Exempt"}
```

### Sheet 2: Annual Basis Calculation
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Partner | Beginning Basis | + Contributions | + Income Items | - Distributions | - Loss Items |
| =Partner_Info!A2 | =VLOOKUP(A2,Prior_Year!A:G,7,0) | =INPUT | =SUMIF(K1_Items!A:A,A2,K1_Items!D:D) | =INPUT | =SUMIF(K1_Items!A:A,A2,K1_Items!E:E) |

| G | H | I | J |
|---|---|---|---|
| + Debt Increase | - Debt Decrease | = Ending Basis | Suspended Losses |
| =INPUT | =INPUT | =MAX(0,B2+C2+D2-E2-F2+G2-H2) | =IF(B2+C2+D2+G2-E2<F2+H2,F2+H2-B2-C2-D2-G2+E2,0) |
```

### Sheet 3: K-1 Item Mapping
```excel
| A | B | C | D | E |
|---|---|---|---|---|
| Partner | K-1 Box | Description | Income Amount | Loss Amount |
| =DROPDOWN | =INPUT | =VLOOKUP(B2,Box_Lookup!A:B,2,0) | =IF(C2>0,C2,0) | =IF(C2<0,ABS(C2),0) |

Box_Lookup Table:
| Box | Description |
|-----|-------------|
| 1 | Ordinary Business Income |
| 2 | Net Rental Real Estate |
| 5 | Interest Income |
| 6a | Ordinary Dividends |
| 8a | Net Short-Term Capital Gain |
| 9a | Net Long-Term Capital Gain |
```

### Sheet 4: Debt Allocation
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Debt Type | Total Amount | Recourse? | Partner | % Share | $ Allocated |
| =INPUT | =INPUT | =DROPDOWN | =Partner_Info!A2 | =IF(C2="Yes",VLOOKUP(D2,Guarantee!A:B,2,0),VLOOKUP(D2,Partner_Info!A:E,5,0)) | =B2*E2 |

Recourse Allocation Formula:
=IF(C2="Yes",
  SUMIF(Guarantees!A:A,D2,Guarantees!B:B)/SUM(Guarantees!B:B)*B2,
  VLOOKUP(D2,Partner_Info!A:E,5,0)*B2)
```

### Sheet 5: State Basis Adjustments
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|
| Partner | Federal Basis | OH Adjustment | IN Adjustment | KY Adjustment | Notes |
| =Partner_Info!A2 | =VLOOKUP(A2,'Annual Basis'!A:I,9,0) | =Federal_State_Diff!B2 | =Federal_State_Diff!C2 | =Federal_State_Diff!D2 | =INPUT |

State Basis Formula:
OH Basis = B2 + C2
IN Basis = B2 + D2
KY Basis = B2 + E2
```

---

## WORKBOOK 2: Multi-State Apportionment Calculator
**Filename**: Multi_State_Apportionment.xlsx

### Sheet 1: Sales Factor
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| State | Gross Sales | Throwback Sales | Net Sales | Total Sales Everywhere | Apportionment % |
| Ohio | =INPUT | =IF(OH_Throwback="Yes",Throwback!B2,0) | =B2+C2 | =SUM(D:D) | =D2/E2 |
| Indiana | =INPUT | =IF(IN_Throwback="Yes",Throwback!B3,0) | =B3+C3 | =E2 | =D3/E3 |
| Kentucky | =INPUT | =IF(KY_Throwback="Yes",Throwback!B4,0) | =B4+C4 | =E2 | =D4/E4 |

Validation Check:
=IF(SUM(F2:F50)>1.001,"ERROR: Apportionment > 100%",IF(SUM(F2:F50)<0.999,"WARNING: Apportionment < 100%","OK"))
```

### Sheet 2: Service Revenue Sourcing
```excel
| A | B | C | D | E |
|---|---|---|---|---|
| Customer | Service Type | Revenue | Benefit State | Sourced Amount |
| =INPUT | =DROPDOWN | =INPUT | =DROPDOWN | =IF(D2="Ohio",C2,0) |

Service Type Dropdown:
={"Consulting";"Software";"Manufacturing";"Professional";"Other"}

Benefit State Dropdown:
={"Ohio";"Indiana";"Kentucky";"Other"}
```

### Sheet 3: Payroll Factor (if applicable)
```excel
| A | B | C | D | E |
|---|---|---|---|---|
| Employee | Total Comp | OH Days | IN Days | KY Days |
| =INPUT | =INPUT | =INPUT | =INPUT | =INPUT |

| F | G | H | I |
|---|---|---|---|
| OH Wages | IN Wages | KY Wages | Check |
| =B2*C2/(C2+D2+E2) | =B2*D2/(C2+D2+E2) | =B2*E2/(C2+D2+E2) | =IF(F2+G2+H2-B2<0.01,"OK","ERROR") |
```

### Sheet 4: Combined Calculation
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| State | Sales Factor | Sales Weight | Payroll Factor | Payroll Weight | Property Factor |
| Ohio | =Sales!F2 | =IF(Single_Sales,"100%","50%") | =Payroll!F2 | =IF(Single_Sales,"0%","25%") | =Property!F2 |
| Indiana | =Sales!F3 | 100% | N/A | 0% | N/A |
| Kentucky | =Sales!F4 | 100% | N/A | 0% | N/A |

| G | H | I |
|---|---|---|
| Property Weight | Total Apportionment | Income Allocated |
| =IF(Single_Sales,"0%","25%") | =B2*C2+D2*E2+F2*G2 | =H2*Total_Income |
```

---

## WORKBOOK 3: S Corporation AAA and Basis Tracker
**Filename**: S_Corp_AAA_Basis.xlsx

### Sheet 1: AAA Account
```excel
| A | B | C | D |
|---|---|---|---|
| Description | Amount | Running AAA | Notes |
| Beginning Balance | =Prior_Year_AAA | =B2 | Prior Year Ending |
| + Ordinary Income | =1120S_Page1_Line21 | =C2+B3 | From Form 1120S |
| + Separately Stated Income | =SUM(K1_Income) | =C3+B4 | Sch K Income Items |
| - Distributions | =MIN(Total_Dist,C4) | =C4-B5 | Limited to AAA |
| - Losses & Deductions | =1120S_Losses | =C5-B6 | Ordinary + Separately Stated |
| - Non-deductible Expenses | =Non_Deduct | =C6-B7 | From M-1 Adjustments |
| Ending AAA | =C7 | =C7 | To Next Year |

AAA Limitation Formula:
=IF(Distributions>AAA_Before_Dist,AAA_Before_Dist,Distributions)
```

### Sheet 2: Shareholder Basis
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Shareholder | Shares | Beginning Stock Basis | + Capital Contributions | + Income Items | - Distributions |
| =INPUT | =INPUT | =Prior_Year!F2 | =INPUT | =K1_Allocation!C2 | =INPUT |

| G | H | I | J | K |
|---|---|---|---|---|---|
| - Loss Items | = Tentative Basis | Losses Limited To | Ending Stock Basis | Suspended Losses |
| =K1_Allocation!D2 | =B2+C2+D2+E2-F2 | =MIN(G2,H2) | =H2-I2 | =G2-I2 |

Debt Basis Calculation:
| L | M | N | O |
|---|---|---|---|
| Beginning Debt Basis | + New Loans | - Repayments | Ending Debt Basis |
| =Prior_Year!O2 | =INPUT | =INPUT | =MAX(0,L2+M2-N2) |
```

### Sheet 3: Distribution Analysis
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Shareholder | Total Distribution | From AAA | From E&P | From Basis | Capital Gain |
| =Basis!A2 | =INPUT | =MIN(B2,AAA_Allocable) | =IF(B2>C2,MIN(B2-C2,EP_Allocable),0) | =IF(B2>C2+D2,MIN(B2-C2-D2,Stock_Basis),0) | =IF(B2>C2+D2+E2,B2-C2-D2-E2,0) |

AAA Allocable Formula:
=AAA_Balance * (Shareholder_Shares/Total_Shares)
```

---

## WORKBOOK 4: Tax Return Review Checklist
**Filename**: Tax_Return_Review_Checklist.xlsx

### Sheet 1: 1040 Review
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Line | Description | Prepared Amount | Reviewed Amount | Variance | Notes |
| 1 | Wages | =INPUT | =INPUT | =C2-B2 | =IF(ABS(D2)>100,"CHECK","OK") |
| 2 | Interest | =INPUT | =INPUT | =C3-B3 | =IF(ABS(D3)>10,"CHECK","OK") |
| 11 | AGI | =SUM(B2:B10) | =SUM(C2:C10) | =C11-B11 | =IF(ABS(D11)>100,"ERROR","OK") |

Effective Tax Rate Check:
=Tax_Owed/Taxable_Income
=IF(Effective_Rate>0.37,"CHECK HIGH",IF(Effective_Rate<0,"CHECK NEGATIVE","OK"))
```

### Sheet 2: K-1 Comparison
```excel
| A | B | C | D | E |
|---|---|---|---|---|---|
| Source | Box | K-1 Amount | Return Amount | Match? |
| ABC Partnership | 1 | =INPUT | =VLOOKUP(A2&B2,Return_Data!A:C,3,0) | =IF(C2=D2,"✓","CHECK") |

Auto-Population from K-1:
=SUMIF(K1_Data!A:A,"Box "&Box_Number,K1_Data!C:C)
```

### Sheet 3: State Reconciliation
```excel
| A | B | C | D | E |
|---|---|---|---|---|---|
| Item | Federal | Ohio | Indiana | Kentucky |
| AGI | =Federal!B11 | =B2+OH_Additions-OH_Subtractions | =B2+IN_Additions-IN_Subtractions | =B2+KY_Additions-KY_Subtractions |
| Additions | | =OH_Addback!Total | =IN_Addback!Total | =KY_Addback!Total |
| Subtractions | | =OH_Deduct!Total | =IN_Deduct!Total | =KY_Deduct!Total |
| State AGI | | =C2 | =D2 | =E2 |
```

---

## WORKBOOK 5: Estimated Tax Calculator
**Filename**: Estimated_Tax_Calculator.xlsx

### Sheet 1: Safe Harbor Analysis
```excel
| A | B | C | D | E |
|---|---|---|---|---|---|
| Jurisdiction | Prior Year Tax | AGI Test | Safe Harbor % | Required Payments |
| Federal | =INPUT | =IF(Prior_AGI>150000,110%,100%) | =C2 | =B2*C2 |
| Ohio | =INPUT | =IF(Prior_AGI>150000,110%,100%) | =C3 | =B3*C3 |
| Indiana | =INPUT | 100% | =C4 | =B4*C4 |
| Kentucky | =INPUT | 100% | =C5 | =B5*C5 |

Current Year Calculation:
| F | G | H |
|---|---|---|
| Projected Tax | 90% Current | Required (Lesser) |
| =Projected_Tax | =F2*0.9 | =MIN(E2,G2) |
```

### Sheet 2: Quarterly Allocation
```excel
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Quarter | Due Date | Federal | Ohio | Indiana | Kentucky |
| Q1 | 4/15/2024 | =Required!H2/4 | =Required!H3/4 | =Required!H4/4 | =Required!H5/4 |
| Q2 | 6/15/2024 | =C2 | =D2 | =E2 | =F2 |
| Q3 | 9/15/2024 | =C2 | =D2 | =E2 | =F2 |
| Q4 | 1/15/2025 | =C2 | =D2 | =E2 | =F2 |
| Total | | =SUM(C2:C5) | =SUM(D2:D5) | =SUM(E2:E5) | =SUM(F2:F5) |

Annualized Income Method (if needed):
=IF(Uneven_Income="Yes",ANNUALIZED_WORKSHEET,EQUAL_INSTALLMENTS)
```

---

## WORKBOOK 6: Error Detection Dashboard
**Filename**: Error_Detection_Dashboard.xlsx

### Sheet 1: Ratio Analysis
```excel
| A | B | C | D | E |
|---|---|---|---|---|---|
| Metric | Current Year | Prior Year | Industry Avg | Flag? |
| Gross Profit Margin | =(Revenue-COGS)/Revenue | =Prior_Year_GPM | =Industry_Data!B2 | =IF(OR(B2<D2*0.8,B2>D2*1.2),"CHECK","OK") |
| Effective Tax Rate | =Tax/Taxable_Income | =Prior_Year_ETR | =Expected_Rate | =IF(ABS(B3-D3)>0.05,"CHECK","OK") |
| Officer Comp/Net Income | =Officer_Comp/Net_Income | =Prior_Year_Ratio | 40% | =IF(B4<0.25,"LOW",IF(B4>0.6,"HIGH","OK")) |

Conditional Formatting:
=IF(E2="CHECK",RED_FILL,IF(E2="OK",GREEN_FILL,YELLOW_FILL))
```

### Sheet 2: Diagnostic Scorecard
```excel
| A | B | C | D |
|---|---|---|---|
| Check Item | Status | Points | Weight |
| Mathematics Verified | =IF(All_Calcs_Check,"PASS","FAIL") | =IF(B2="PASS",1,0) | 25% |
| Prior Year Matched | =IF(PY_Match,"PASS","FAIL") | =IF(B3="PASS",1,0) | 20% |
| K-1s Reconciled | =IF(K1_Recon,"PASS","FAIL") | =IF(B4="PASS",1,0) | 20% |
| States Complete | =IF(States_Done,"PASS","FAIL") | =IF(B5="PASS",1,0) | 15% |
| Documentation Complete | =IF(Docs_Complete,"PASS","FAIL") | =IF(B6="PASS",1,0) | 20% |
| Total Score | | =SUMPRODUCT(C2:C6,D2:D6) | 100% |

Overall Rating:
=IF(C7>=0.9,"READY TO FILE",IF(C7>=0.7,"NEEDS REVIEW","INCOMPLETE"))
```

---

## MACRO FORMULAS FOR AUTOMATION

### Auto-Import K-1 Data
```vba
Sub ImportK1Data()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("K1_Input")
    
    'Loop through K-1 boxes
    For i = 1 To 20
        BoxValue = ws.Range("B" & i).Value
        'Map to appropriate line on return
        Select Case i
            Case 1: Sheets("SchE").Range("B5").Value = BoxValue
            Case 2: Sheets("SchE").Range("B7").Value = BoxValue
            'Continue mapping...
        End Select
    Next i
End Sub
```

### Basis Limitation Check
```vba
Function CheckBasisLimit(Loss As Double, Basis As Double) As Double
    If Loss > Basis Then
        CheckBasisLimit = Basis
        MsgBox "Loss limited to basis of " & Format(Basis, "Currency")
    Else
        CheckBasisLimit = Loss
    End If
End Function
```

### State Apportionment Validation
```vba
Function ValidateApportionment(StateFactors As Range) As String
    Total = Application.Sum(StateFactors)
    If Total > 1.001 Then
        ValidateApportionment = "ERROR: >100%"
    ElseIf Total < 0.999 Then
        ValidateApportionment = "WARNING: <100%"
    Else
        ValidateApportionment = "OK"
    End If
End Function
```

---

## IMPLEMENTATION TIPS

### Setting Up the Workbooks

1. **Create Master Template**
   - Save as .xltx for reuse
   - Lock formulas with protection
   - Include instruction sheets

2. **Link Between Workbooks**
   ```excel
   ='[Partnership_Basis_Tracker.xlsx]Annual Basis'!$I$2
   ```

3. **Create Named Ranges**
   ```excel
   Name: Federal_AGI
   Refers to: =1040_Review!$B$11
   ```

4. **Add Data Validation**
   ```excel
   Data > Validation > List
   Source: =States_List
   ```

5. **Conditional Formatting Rules**
   - Red: Errors requiring immediate attention
   - Yellow: Warnings to review
   - Green: Passed checks

### Best Practices

1. **Version Control**
   - Save as "ClientName_TaxYear_v1.xlsx"
   - Keep prior versions for reference

2. **Documentation**
   - Add comments to complex formulas
   - Include assumption notes
   - Document manual overrides

3. **Review Process**
   - Preparer completes input tabs
   - Reviewer checks formula tabs
   - Partner reviews dashboard

4. **Backup Strategy**
   - Save to network drive
   - Create PDF snapshots
   - Export key data to CSV

These Excel templates provide automated calculations and error checking for your tax return review process. Each workbook can be customized for specific client needs while maintaining standardized formulas and review procedures.