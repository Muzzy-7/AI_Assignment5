# AI-Based Travel Planner using Multiple Knowledge Bases

## Overview

This project proposes an AI-Based Travel Planner that reuses information from multiple existing Knowledge Bases (KBs) to generate personalized travel recommendations. The system integrates tourism, hotel, food, and weather knowledge sources into a unified Knowledge Graph and recommends the best travel plan based on user preferences and budget constraints.

---

# Objectives

* Reuse existing Knowledge Bases for travel planning.
* Integrate information from multiple domains.
* Understand user preferences and interests.
* Generate personalized travel recommendations.
* Perform cost assessment and budget validation.
* Suggest the optimal travel plan.

---

# High-Level Architecture

```text
                    User Preferences
      (Budget, Interests, Food, Duration)
                               │
                               ▼
                    Preference Analyzer
                               │
                               ▼
                 Knowledge Integration Layer
 ┌─────────────────────────────────────────────────┐
 │                                                 │
 │ Tourism KB      Hotel KB      Food KB          │
 │ Attractions     Hotels        Restaurants      │
 │ Activities      Prices        Cuisine          │
 │                                                 │
 │ Weather KB      Location KB                    │
 │ Climate         Maps & Distance                │
 └─────────────────────────────────────────────────┘
                               │
                               ▼
                    Unified Knowledge Graph
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

# Existing Knowledge Bases Reused

## Tourism Knowledge Base

Contains:

* Tourist attractions
* Historical monuments
* Adventure activities
* Cultural locations

Example:

```text
(Eiffel Tower, locatedIn, Paris)
(Amber Fort, locatedIn, Jaipur)
```

---

## Hotel Knowledge Base

Contains:

* Hotel information
* Room prices
* Ratings
* Facilities

Example:

```text
(Hotel Paradise, locatedIn, Goa)
(Hotel Paradise, costPerNight, 3500)
```

---

## Food Knowledge Base

Contains:

* Restaurants
* Local cuisines
* Dietary information

Example:

```text
(Goa, famousFor, Seafood)
(Jaipur, famousFor, Dal Baati)
```

---

## Weather Knowledge Base

Contains:

* Seasonal information
* Temperature
* Climate conditions

Example:

```text
(Manali, climate, Cold)
(Goa, climate, Tropical)
```

---

## Location Knowledge Base

Contains:

* Distances
* Routes
* Geographic information

Example:

```text
(Delhi, connectedTo, Jaipur)
```

---

# Knowledge Graph Representation

The integrated information is represented as a Knowledge Graph.

### Entities

```text
User
City
TouristPlace
Hotel
Restaurant
Activity
```

### Relationships

```text
LIKES
LOCATED_IN
HAS_ACTIVITY
HAS_HOTEL
HAS_FOOD
CONNECTED_TO
```

Example:

```text
(User)
   │
LIKES
   │
(History)
   │
HAS_ACTIVITY
   │
(Amber Fort)
   │
LOCATED_IN
   │
(Jaipur)
```

---

# Working Process

1. User enters preferences such as:

   * Budget
   * Destination type
   * Food preference
   * Travel duration

2. Preference Analyzer extracts user requirements.

3. Knowledge Integration Layer retrieves information from existing Knowledge Bases.

4. Retrieved information is combined into a unified Knowledge Graph.

5. Recommendation Engine identifies suitable destinations, attractions, hotels, and restaurants.

6. Cost Assessment Module estimates the total travel expense.

7. The system selects the best travel plan that satisfies user preferences and budget constraints.

---

# Cost Assessment

The total trip cost is calculated as:

```text
Total Cost =
Travel Cost +
Hotel Cost +
Food Cost +
Local Transport +
Entry Fees
```

Constraint:

```text
Total Cost ≤ User Budget
```

---

# Sample Output

```text
User Preferences

Interest      : Historical Tourism
Food          : Vegetarian
Budget        : ₹50,000
Duration      : 4 Days

Recommended Travel Plan

Destination:
Jaipur

Tourist Places:
• Amber Fort
• Hawa Mahal
• City Palace

Hotel:
Heritage Residency

Food:
Dal Baati Churma

Estimated Cost:
₹46,500

Status:
Within Budget
```

---

# Technologies Used

| Component                | Technology      |
| ------------------------ | --------------- |
| Programming Language     | Python          |
| Knowledge Representation | Knowledge Graph |
| Ontology Tool            | Protégé         |
| Graph Database           | Neo4j           |
| Query Language           | Cypher / SPARQL |

---

# Advantages

* Reuses existing knowledge instead of creating data from scratch.
* Integrates multiple domains into a single system.
* Provides personalized recommendations.
* Performs efficient travel planning.
* Supports budget-aware decision making.

---

# Conclusion

The proposed AI-Based Travel Planner combines and reuses information from multiple Knowledge Bases including tourism, hotel, food, weather, and location sources. By integrating these sources into a unified Knowledge Graph and performing cost assessment, the system generates personalized and budget-friendly travel plans that best satisfy user preferences.
