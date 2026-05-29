# Bayesian Networks: Modeling, Inference, and Tools

## What is Bayesian Network
A Bayesian Network (BN) is a probabilistic model represented as a Directed Acyclic Graph (DAG). The nodes represent random variables, while the edges show probabilistic dependencies between them. Each node contains a Conditional Probability Distribution (CPD) that defines how it depends on its parent nodes.

The main advantage of a BN is that it represents complex probability distributions efficiently. Instead of storing the entire joint probability distribution, the network stores only the CPDs, reducing both storage and computation requirements.

Main Operations in a Bayesian Network

Bayesian Networks are mainly used for three tasks:

Modeling: Defining relationships between variables either manually using domain knowledge or automatically through structure learning algorithms.
Inference: Calculating probabilities when some evidence is known.
Learning: Estimating CPD values from data using methods such as Maximum Likelihood Estimation (MLE) or Bayesian Estimation.
Tools and Libraries

Several tools are available for working with Bayesian Networks.

pgmpy – Python library for modeling, learning, and inference.
bnlearn – Popular package available in both R and Python.
pyAgrum – Useful for dynamic Bayesian Networks.
Tetrad – GUI-based tool for causal discovery and network design.
CDT and gCastle – Libraries focused on causal discovery.

Among these, pgmpy was used for this implementation because it provides support for network creation, parameter learning, and multiple inference algorithms.

### Implementation Overview

This project implements the classic Burglary–Alarm Bayesian Network using pgmpy.

The network contains five variables:

* Burglary
* Earthquake
* Alarm
* JohnCalls
* MaryCalls

The model demonstrates how evidence affects probability calculations and highlights the explaining-away effect, where one cause can reduce the probability of another cause once evidence is observed.

The script performs the following tasks:

Builds the Bayesian Network and defines CPDs.
Runs exact inference using Variable Elimination.
Runs Belief Propagation for comparison.
Uses Forward Sampling to approximate probabilities.
Generates synthetic data and learns CPDs using MLE.
