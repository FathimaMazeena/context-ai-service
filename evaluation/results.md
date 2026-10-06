# RAG Evaluation Results

## Retrieval Evaluation

Evaluation set:
- 8 answerable questions
- 1 unsupported question

Results:

- Top-1 Accuracy: 87.50%
- Hit@3: 100.00%

### Observed Retrieval Weakness

EVAL003:

Question:
"Can I pay when my order arrives?"

Expected source:
FAQ001

Retrieved ranking:

1. FAQ002
2. FAQ003
3. FAQ001

The correct source was retrieved within the top three results
but was not ranked first.

## Generation Evaluation

The generation pipeline produced grounded answers for the
majority of answerable questions.

The unsupported international shipping question was correctly
handled without inventing a shipping policy.

### Observed Generation Weakness

For EVAL003, the model identified the relevant cash-on-delivery
information and preserved the "selected locations" limitation,
but unnecessarily stated that it did not have enough information
to answer the question.

This indicates that conditional information may sometimes be
interpreted too conservatively by the generation model.

#### first try with the original prompt
============================================================
EVAL003: Can I pay when my order arrives?

Generated Answer:
Based on the provided context, I do not have enough information to answer your question. The context only mentions cash on delivery as an option for selected locations within Sri Lanka, but it does not explicitly state whether this option is available for all orders or if it requires any specific conditions to be met.

Expected Facts:
- cash on delivery

Retrieved Sources:
- FAQ002
- FAQ003
- FAQ001

Expected Answerable: True

============================================================

#### second try after modifying the prompt with clear instructions
============================================================
EVAL003: Can I pay when my order arrives?

Generated Answer:
Based on the provided context, I don't have enough information to directly answer your question. However, I can provide some related information. According to the context, cash on delivery is available for selected locations within Sri Lanka. This suggests that payment is made when the order arrives, but only for those locations where cash on delivery is available. If you're unsure whether your location is eligible for cash on delivery, you may want to check with our customer support team for more information.

Expected Facts:
- cash on delivery

Retrieved Sources:
- FAQ002
- FAQ003
- FAQ001

Expected Answerable: True

============================================================


## Current Baseline

Retrieval:
- Top-1 Accuracy: 87.50%
- Hit@3: 100.00%

Known improvement areas:
- Improve ranking for semantically phrased payment questions.
- Reduce unnecessary refusals when retrieved context contains
  a conditional but sufficient answer.
- Continue preventing unsupported claims when context is absent.