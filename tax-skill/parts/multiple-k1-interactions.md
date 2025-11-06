# Multiple K-1 Interaction Review Guide

## Overview
This guide addresses the complex interactions when a taxpayer has multiple K-1s with varying characteristics: self-rentals, passive/non-passive activities, QBI eligibility, and basis limitations. The order of analysis matters significantly.

## Step-by-Step Analysis Framework

### Step 1: K-1 Inventory and Classification

Create a master grid for ALL K-1s:

| Entity | Type | Box 1 | Self-Rental? | Material Part? | QBI Eligible? | Basis | At-Risk | PAL Status |
|--------|------|-------|--------------|----------------|---------------|-------|---------|------------|
| ABC LLC | 1065 | (50k) | No | Yes | Yes | 75k | 75k | Non-passive |
| DEF LP | 1065 | 30k | No | No | No | 100k | 0 | Passive |
| GHI Properties | 1065 | (20k) | Yes-to ABC | N/A | No | 40k | 40k | See reclass |
| JKL Holdings | 1120S | 15k | No | Yes | Yes | 60k | 60k | Non-passive |

### Step 2: Self-Rental Recharacterization Rules

**Critical**: Self-rental rules override normal passive activity rules

#### Self-Rental Income Recharacterization
```
IF: Rental property rented to entity where taxpayer materially participates
AND: Net rental income (positive)
THEN: Income recharacterized as NON-PASSIVE

IF: Net rental loss
THEN: Remains passive (no recharacterization of losses)
```

#### Common Self-Rental Patterns
1. **Real Estate LLC → Operating Business**
   - Building owned by LLC A, rented to S Corp B
   - Taxpayer materially participates in S Corp B
   - Rental profit = non-passive
   - Rental loss = passive

2. **Complex Tiered Structures**
   - Property LLC → Management LLC → Operating LLC
   - Trace through to ultimate use
   - Document material participation at operating level

### Step 3: Passive Activity Grouping Analysis

#### Grouping Elections (Critical for Planning)
**Regulation 1.469-4 Allows Grouping If:**
- Same line of business
- Common control
- Geographic proximity
- Interdependence

**Self-Rental Grouping Opportunity:**
```
Property LLC (rental loss) + Operating Entity (active income)
IF properly grouped → Single activity
Result: Rental loss becomes non-passive if materially participate
```

**Document Grouping Elections:**
- Must be consistent year-to-year
- File disclosure statement in year of grouping
- Consider state implications (some states don't recognize)

### Step 4: Material Participation Testing (Per Activity)

Run tests for EACH non-grouped activity:

| Test | Hours Required | ABC LLC | JKL Holdings | 
|------|---------------|---------|--------------|
| 1. 500 hours | 500+ | ✓ 650 hrs | ✓ 520 hrs |
| 2. Substantially all | ~All participation | No | No |
| 3. >100 hrs & most | 100+ & more than others | No | Yes |
| 4. Significant participation | Aggregate >500 | N/A | N/A |
| 5. Material 5 of 10 years | 5 prior years | Yes | Yes |

### Step 5: Basis and At-Risk Limitations (Per K-1)

**Order of Limitations (CRITICAL):**
1. Tax Basis
2. At-Risk Amount  
3. Passive Activity Loss Rules
4. Excess Business Loss Limitation

#### Multi-Tiered Basis Tracking
```
Upper Tier Entity Basis:
Beginning Basis                 $100,000
+ Capital contributions          $20,000
+ Share of lower tier income     $15,000
- Distributions received        ($30,000)
- Share of lower tier loss      ($25,000)
= Ending Basis                   $80,000

Lower Tier Limitation:
Lower tier K-1 loss             ($40,000)
Upper tier basis available       $80,000
Loss allowed at upper tier      ($40,000)
```

#### Debt Basis Considerations
- **S Corps**: Only direct loans create debt basis
- **Partnerships**: Share of entity debt increases basis
- **Self-Rentals**: Mortgage on rental property affects basis

### Step 6: QBI Analysis with Multiple K-1s

#### QBI Qualification Matrix

| Entity | Trade/Business? | SSTB? | W-2 Wages | UBIA | Box 20 Code Z |
|--------|----------------|-------|-----------|------|---------------|
| ABC LLC | Yes | No | $200k | $500k | $50k |
| DEF LP | No (Investment) | N/A | $0 | $0 | $0 |
| GHI Properties | Yes | No | $0 | $800k | $(20k) |
| JKL Holdings | Yes | Yes | $150k | $100k | $15k |

#### QBI Aggregation Rules
**Can Aggregate If:**
1. Same tax year
2. Common control (50%+)
3. Meet 2 of 3 factors:
   - Same products/services
   - Shared facilities/operations  
   - Interdependent businesses

**Aggregation Benefits:**
- Combine W-2 wages and UBIA
- Offset QBI losses with QBI income
- Optimize wage/property limitations

### Step 7: Loss Ordering Rules

When losses exceed basis or are passive limited:

1. **Current Year Losses**
   ```
   Total K-1 Losses:           $(100,000)
   Basis Limitation:           $  75,000
   Allowed Current:            $( 75,000)
   Suspended - Basis:          $( 25,000)
   ```

2. **Prior Year Suspended Losses**
   ```
   Prior Suspended - Basis:    $( 30,000)
   Prior Suspended - At-Risk:  $( 10,000)
   Prior Suspended - Passive:  $( 45,000)
   Current Year Passive Income: $  20,000
   Released Passive Losses:    $( 20,000)
   ```

3. **Carryforward Tracking**
   - Track by entity
   - Track by limitation type
   - Track by year

### Step 8: State Tax Complications

#### Multi-State K-1 Issues
**Different State Rules:**
- Basis adjustments (bonus depreciation)
- Passive activity rules
- Entity-level taxes
- Composite returns

**State Modification Tracking:**
```
Federal K-1 Box 1:           $(50,000)
Ohio Add-back (bonus dep):   $ 15,000
Ohio Adjusted Loss:          $(35,000)
Indiana (no modification):   $(50,000)
Kentucky LLET paid:          $  2,000
Kentucky Adjusted:           $(48,000)
```

## Complex Interaction Scenarios

### Scenario 1: Self-Rental with Operating Loss
```
Real Estate LLC:
- Rental income to related S Corp: $100,000
- Depreciation and expenses: $(80,000)
- Net income: $20,000
- Recharacterized as: NON-PASSIVE

S Corp (tenant):
- Operating loss: $(150,000)
- Material participation: YES
- Character: NON-PASSIVE

Result: $20,000 non-passive income offsets operating loss
```

### Scenario 2: Passive Loss with QBI
```
Partnership A:
- Ordinary loss: $(75,000)
- QBI: $(75,000)
- Passive activity: YES
- Current year deduction: $0 (suspended)
- QBI impact: $(75,000) carries forward

Partnership B:
- Ordinary income: $50,000
- QBI: $50,000
- Passive activity: YES

Net Result:
- Passive income: $50,000
- Release suspended loss: $(50,000)
- Net taxable: $0
- Net QBI: $(25,000) suspended
```

### Scenario 3: Basis Limitation with Multiple Tiers
```
Top-Tier Partnership:
- K-1 from Lower-Tier: $(100,000)
- Direct expenses: $(20,000)
- Partner basis: $90,000

Allowable Loss:
- Lower-tier loss limited: $(90,000)
- Direct expenses: $(20,000)
- Total limited to basis: $(90,000)
- Suspended: $(30,000)
```

## Review Checklist for Multiple K-1s

### Initial Classification
- [ ] List all K-1s with entity names and EINs
- [ ] Identify entity types (1065, 1120S, etc.)
- [ ] Mark self-rental relationships
- [ ] Note material participation status
- [ ] Identify QBI eligibility
- [ ] Document grouping elections

### Basis and Limitation Tracking
- [ ] Calculate beginning basis for each
- [ ] Apply current year adjustments
- [ ] Determine at-risk amounts
- [ ] Calculate allowable losses
- [ ] Track suspended amounts by type

### Passive Activity Analysis
- [ ] Complete material participation tests
- [ ] Apply self-rental recharacterization
- [ ] Match passive income with losses
- [ ] Calculate suspended PALs
- [ ] Document grouping elections

### QBI Optimization
- [ ] Identify QBI entities
- [ ] Calculate W-2 wages per entity
- [ ] Determine UBIA of qualified property
- [ ] Consider aggregation election
- [ ] Apply SSTB limitations
- [ ] Calculate taxable income limitation

### State Tax Considerations
- [ ] Apply state modifications
- [ ] Track state basis separately
- [ ] Consider composite returns
- [ ] Calculate PTE tax elections
- [ ] Verify apportionment

## Common Pitfalls with Multiple K-1s

1. **Self-Rental Losses Not Limited**
   - Error: Deducting rental losses against active income
   - Fix: Losses remain passive despite self-rental

2. **Incorrect Grouping**
   - Error: Informal grouping without election
   - Fix: File disclosure, maintain consistency

3. **Basis Confused Across Entities**
   - Error: Using wrong entity's basis
   - Fix: Track separately by K-1

4. **QBI Netting Errors**
   - Error: Offsetting QBI loss against non-QBI income
   - Fix: QBI losses only offset QBI income

5. **State Basis Mismatches**
   - Error: Using federal basis for state
   - Fix: Maintain separate calculations

## Documentation Requirements

### For Each K-1 Maintain:
1. **Basis Schedule**
   - Beginning, current, ending
   - Federal and each state

2. **Passive Activity Log**
   - Hours by activity
   - Material participation tests
   - Grouping elections

3. **Loss Carryforward Schedule**
   - By entity
   - By limitation type
   - By year

4. **QBI Tracking**
   - Current and carryforward
   - Aggregation elections
   - W-2 wage/UBIA calculations

5. **Self-Rental Documentation**
   - Lease agreements
   - Ownership percentages
   - Material participation proof

## Excel Formula Helpers

### Passive Loss Limitation
```excel
=MIN(0,IF(MaterialParticipation="Yes",Loss,
  MAX(Loss,-PassiveIncome)))
```

### Basis Limitation
```excel
=MAX(-BeginningBasis-Contributions+Distributions,Loss)
```

### QBI Aggregation Test
```excel
=IF(AND(CommonControl>=0.5,
  COUNTIF(TestRange,"Yes")>=2),"Eligible","Not Eligible")
```

### Self-Rental Recharacterization
```excel
=IF(AND(SelfRental="Yes",RentalIncome>0,
  MaterialParticipationInTenant="Yes"),"Non-Passive","Passive")
```

## Planning Opportunities

1. **Timing Distributions**
   - Take before year-end to reduce basis
   - Suspend losses for future income

2. **Grouping Elections**
   - Group to unlock suspended losses
   - Separate to preserve QBI

3. **Material Participation Planning**
   - December push to reach 500 hours
   - Document contemporaneously

4. **State PTE Elections**
   - Coordinate across entities
   - Consider federal benefit vs. state cost

5. **QBI Optimization**
   - Aggregate strategically
   - Time income/deductions
   - Consider wage strategies