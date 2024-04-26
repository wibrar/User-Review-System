### Comparison to Existing Architecture
Since we mostly tried to follow SRP design principles for our project, with each module 
taking care of itself and by splitting each module into different classes to perform different
tasks, it didn’t feel difficult to describe our project as a microservice. However, in comparison 
to our UML architecture, it would have been even more split up. For example, instead of just having 
a “Review” module, we would have split this into all of its services. This might have been a big help
for us at the start of the sprint, when we were still figuring things out- perhaps thinking in terms of 
“what services should this provide?” would have helped us plan out all the methods farther in advance.
   
Another big change would be with the database. In matching with microservice architecture, we
likely would have looked into giving each service its own database instead of storing them all 
in the same database as we are now. For example, accounts would be stored in one database, and 
reviews in another. This would lead to more separation between data, and probably would have made
debugging database issues a lot easier in retrospect.

### Proposed impact of a microservice architecture on software process
If we had followed a microservice architecture process for our software from the beginning, 
we would have had a lot less “crossing over” in terms of working on methods in other modules. 
I believe that, if this had been our design from the beginning, we would have planned our 
project at the beginning by assigning each team member one or two microservices. 
Firstly, this would have allowed each developer to work in a more contained environment and 
their resultant product would necessarily have minimum dependence on any other component 
in the software system. Additionally, our process would have benefited from this by making
bug-fixing more efficient as any bug would have been contained to a particular microservice. 
Each microservice developer would have additionally been responsible for creating their
own HTML pages, and this would have lessened the workload on our frontend developer by 
distributing the tasks evenly across the group. This would have also allowed each team 
member to fully express their vision of the particular feature they were working on, and 
thus avoid the dilemma of working on a feature with an inconsistent vision of the final product,
and then having to devote time to fine-tuning the feature. Finally, each team member would have
been able to work in parallel, as no member would have to wait for another member to implement 
stub methods or complete their task

![Diagram 2023-12-12 15-56-30.png](UML_Diagrams%2FDiagram%202023-12-12%2015-56-30.png)