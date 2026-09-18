
# ------------Retrieval Methods --------------

| Method                      | Simple meaning                                           | Example                                             |
| --------------------------- | -------------------------------------------------------- | --------------------------------------------------- |
| **1. Levenshtein distance** | Handles **typos/spelling mistakes**                      | `cancer` ↔ `cancr`                                  |
| **2. Jaccard similarity**   | Checks **how many words overlap**                        | `EGFR cancer treatment` ↔ `EGFR treatment options`  |
| **3. TF-IDF**               | Gives more importance to **important/rare keywords**     | `EGFR` may matter more than `the`                   |
| **4. Word vectors**         | Finds **similar meaning**, even when words differ        | `lung tumor` ↔ `lung cancer`                        |
| **5. Toy neural ranker**    | A small ML model **learns what makes a result relevant** | Learns that `EGFR + osimertinib` is highly relevant |
| **6. Hybrid retrieval**     | **Combines several methods**                             | typo + keyword + meaning + learned relevance        |
