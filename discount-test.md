

| Type of test | Test | Value | Expected result | Comment |
| --- | --- | --- | --- | --- |
| Normal | Testing normal combinations price / discount | Price: 20Discount: 10 | 18 |   |
|   |   | Price: 40Discount: 10 | 36 |   |
|   |   | Price: 20Discount: 25 | 15 |   |
|   |   | Price: 40Discount: 25 | 30 |   |
| Extreme | Testing zero price / normal discount | Price: 0Discount: 25 | 0 |   |
|   | Test normal price / zero discount | Price: 40Discount: 0 | 40 |   |
|   | Test normal price / 100% discount | Price: 40Discount: 100 | 0 |   |
| Exceptional | Negative Price | Price: -10 | Error message, ask again |   |
|   | Negative discount | Price: normal valueDiscount: -50 | Error message, ask again |   |
|   | Discount over 100% | Price: normal valueDiscount: 150% |   |   |
|   |   |   |   |   |
|   |   |   |   |   |

