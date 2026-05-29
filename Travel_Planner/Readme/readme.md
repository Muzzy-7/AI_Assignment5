# AI-Based Travel Planner using Knowledge Bases

---

## Objectives

* Integrate multiple Knowledge Bases for travel planning.
* Understand user preferences and interests.
* Generate personalized travel recommendations.
* Estimate travel expenses.
* Select the best travel plan within the user's budget.

---

## High-Level Architecture

```text
User Preferences
      │
      ▼
Preference Analyzer
      │
      ▼
Knowledge Integration Layer
 ┌─────────┬─────────┬─────────┐
 │Tourism  │ Food KB │ Hotel KB│
 │   KB    │         │         │
 └─────────┴─────────┴─────────┘
      │
      ▼
Recommendation Engine
      │
      ▼
Cost Assessment Module
      │
      ▼
Optimal Travel Plan
```

---

## Knowledge Bases Used

### Tourism Knowledge Base

Stores information about:

* Cities
* Tourist attractions
* Activities
* Historical sites

### Food Knowledge Base

Stores information about:

* Restaurants
* Local cuisines
* Dietary preferences
* Food ratings

### Hotel Knowledge Base

Stores information about:

* Hotels
* Accommodation costs
* Ratings
* Facilities

---

## Working Process

1. User enters destination preferences, interests, budget, and dietary requirements.
2. The Preference Analyzer extracts important requirements.
3. The Knowledge Integration Layer gathers information from multiple Knowledge Bases.
4. The Recommendation Engine identifies suitable destinations, attractions, hotels, and restaurants.
5. The Cost Assessment Module calculates the total estimated cost.
6. The system selects the best travel plan satisfying user preferences and budget constraints.

---

## Cost Assessment

Total trip cost is calculated as:

```text
Total Cost = Travel Cost + Hotel Cost + Food Cost + Local Transport + Entry Fees
```

Constraint:

```text
Total Cost ≤ User Budget
```

---

## Technologies Used

| Component                | Technology      |
| ------------------------ | --------------- |
| Programming Language     | Python          |
| Knowledge Representation | Knowledge Graph |
| Ontology Tool            | Protégé         |
| Graph Database           | Neo4j           |
| Query Language           | Cypher/SPARQL   |

---

## Sample Output

```text
User Preferences:
Destination Type = Historical
Budget = ₹50,000
Food Preference = Vegetarian

Recommended Plan:

Destination: Jaipur
Tourist Places:
- Amber Fort
- Hawa Mahal

Hotel:
- Heritage Residency

Food:
- Dal Baati Churma

Estimated Cost:
₹46,500

Status:
Within Budget
```

---

## Conclusion

The proposed AI-Based Travel Planner combines multiple Knowledge Bases to generate intelligent travel recommendations. By integrating tourism, hotel, and food knowledge with cost assessment, the system produces personalized and budget-friendly travel plans.
