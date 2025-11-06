# Self-Rental Decision Tree Flowchart

## Main Decision Tree

```
START: Is there a rental payment between related entities?
│
├─NO→ Not a self-rental issue → Apply normal passive rules
│
└─YES→ Continue to next question
      │
      ▼
      Are the entities related through common ownership?
      │
      ├─NO→ Not self-rental → Apply normal passive rules
      │
      └─YES→ What is the ownership structure?
            │
            ▼
            [Ownership Analysis Branch]
```

## Ownership Analysis Branch

```
What is the ownership percentage?
│
├─ Same person/entity owns both → Definitely self-rental
│
├─ >50% common ownership → Likely self-rental
│
├─ 25-50% common ownership → Possible self-rental (check facts)
│
└─ <25% common ownership → Unlikely self-rental
    │
    ▼
    Check attribution rules (family, entities)
    │
    ├─ With attribution >50% → Self-rental applies
    │
    └─ With attribution <50% → Not self-rental
```

## Material Participation Test Branch

```
Does the taxpayer materially participate in the TENANT entity?
│
├─NO→ Rental remains passive (no recharacterization)
│     │
│     └→ END: Normal passive activity rules apply
│
└─YES→ Continue to income/loss determination
      │
      ▼
      [Income/Loss Branch]
```

## Income/Loss Determination Branch

```
Is the rental activity generating net income or loss?
│
├─ NET INCOME (Positive)
│   │
│   └→ RECHARACTERIZE AS NON-PASSIVE
│      │
│      ├→ Impact: Rental income becomes non-passive
│      ├→ Cannot offset passive losses from other activities
│      ├→ Can offset with non-passive losses
│      └→ Document recharacterization
│
└─ NET LOSS (Negative)
    │
    └→ REMAINS PASSIVE
       │
       ├→ Impact: Cannot offset against active income
       ├→ Can only offset passive income
       ├→ May be suspended as PAL
       └→ Consider grouping election
```

## Grouping Election Decision Branch

```
Is there a rental loss that could benefit from grouping?
│
├─NO→ No grouping needed
│
└─YES→ Evaluate grouping eligibility
      │
      ▼
      Do the activities constitute an appropriate economic unit?
      │
      ├─NO→ Cannot group → Loss remains passive
      │
      └─YES→ Check five factors:
            │
            ├─ 1. Similarities (same/similar business?)
            ├─ 2. Common control (same ownership?)
            ├─ 3. Common ownership (% overlap?)
            ├─ 4. Geographic location (proximity?)
            └─ 5. Interdependence (rely on each other?)
                  │
                  ▼
                  Do 2+ factors support grouping?
                  │
                  ├─NO→ Weak case for grouping
                  │
                  └─YES→ Grouping allowed
                        │
                        ▼
                        [Grouping Implementation Branch]
```

## Grouping Implementation Branch

```
Has a grouping election been made previously?
│
├─YES→ Must maintain consistency
│     │
│     └→ Is current treatment consistent?
│        │
│        ├─YES→ Continue with grouped treatment
│        │
│        └─NO→ Need to explain change
│              │
│              └→ File disclosure statement
│
└─NO→ Make initial grouping election
     │
     ├→ File disclosure with return
     ├→ Document business purpose
     ├→ Maintain for future years
     └→ Consider state implications
```

## Multiple Entity Complexity Branch

```
Are there multiple rental properties or tenant entities?
│
├─NO→ Apply single entity analysis above
│
└─YES→ Analyze EACH relationship separately
      │
      ▼
      For EACH rental-tenant pair:
      │
      ├─ Property A → Tenant 1
      │   ├─ Material participation in Tenant 1?
      │   ├─ Net income or loss from Property A?
      │   └─ Apply recharacterization rules
      │
      ├─ Property A → Tenant 2
      │   ├─ Material participation in Tenant 2?
      │   ├─ Allocate income/loss proportionally
      │   └─ Apply rules to allocated portion
      │
      └─ Property B → Tenant 1
          ├─ Separate analysis required
          ├─ Cannot net with Property A
          └─ Track separately
```

## State Tax Treatment Branch

```
What states are involved?
│
├─ OHIO
│   ├─ Follows federal self-rental treatment
│   ├─ Consider CAT tax implications
│   └─ Municipal tax may differ
│
├─ INDIANA
│   ├─ Generally follows federal
│   ├─ Check county tax implications
│   └─ Consider throwback rules
│
└─ KENTUCKY
    ├─ May not recognize grouping
    ├─ LLET applies regardless
    └─ Check local tax treatment
```

## Documentation Requirements Checklist

```
Required Documentation for Self-Rental:
│
├─ □ Lease agreement between entities
├─ □ Ownership structure documentation
├─ □ Material participation evidence (hours, duties)
├─ □ Fair market rent analysis
├─ □ Business purpose documentation
├─ □ Grouping election (if applicable)
├─ □ Prior year consistency check
└─ □ State treatment analysis
```

## Quick Decision Matrix

| Scenario | Material Part in Tenant? | Rental Income/Loss | Result |
|----------|-------------------------|-------------------|---------|
| 1 | Yes | Income | Non-Passive |
| 2 | Yes | Loss | Passive |
| 3 | No | Income | Passive |
| 4 | No | Loss | Passive |
| 5 | Yes (grouped) | Loss | Non-Passive |

## Red Flags for Audit Risk

```
HIGH RISK indicators requiring extra documentation:
│
├─ Rental loss + high tenant income → Why not grouped?
├─ Below-market rent → Related party transaction scrutiny
├─ Inconsistent treatment year-to-year → Need explanation
├─ Multiple entities with different treatment → Document each
└─ State treatment differs from federal → Explain why
```

## Planning Opportunities Decision Points

```
Should we make a grouping election?
│
├─ Current year rental loss? → YES, consider grouping
├─ Future rental losses expected? → YES, consider grouping
├─ Tenant has consistent profits? → YES, likely beneficial
├─ Planning to sell property? → NO, keep separate
├─ State doesn't recognize grouping? → NO, adds complexity
└─ QBI implications? → ANALYZE, may want separate

Should we restructure?
│
├─ Consistent rental losses? → Consider restructuring ownership
├─ Multiple properties? → Consider separate entities
├─ State tax issues? → May benefit from restructuring
└─ Exit strategy planned? → Keep flexibility
```

## Common Errors to Avoid

```
ERROR CHECKPOINT - Do NOT:
│
├─ ✗ Assume all related rentals are self-rental
├─ ✗ Recharacterize rental losses as non-passive
├─ ✗ Group without proper election
├─ ✗ Change grouping without disclosure
├─ ✗ Ignore state differences
├─ ✗ Net multiple properties without analysis
├─ ✗ Forget to track suspended losses
└─ ✗ Miss documentation requirements
```

## Year-End Planning Checklist

```
Before December 31:
│
├─ □ Calculate projected rental income/loss
├─ □ Evaluate material participation hours
├─ □ Consider accelerating expenses if income
├─ □ Consider deferring expenses if loss
├─ □ Review grouping election benefit
├─ □ Document any changes
├─ □ Plan for state tax implications
└─ □ Consider distribution timing
```
