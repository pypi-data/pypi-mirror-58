
----------------------------------------------------------------------------------------------------------------------------------
OWL constructor        DL               Manchester         [Python][Owlready2]        Read                  Meaning
---------------------  ---------------  -----------------  -------------------        -------------------   --------------------
owl:Thing              $\top$                              Thing                      top                   A special class with every individual as an instance

owl:Nothing            $\bot$                              Nothing                    bottom                The empty class

                       $A\doteq B$                                                    A is defined to be    Class *definition*
                                                                                      equal to B

rdf:subclassOf         $A\sqsubseteq B$ A subclass_of B    class A(B): ...            all A are B           Class *inclusion*

                                                           issubclass(A, B)                                 Test for inclusion

owl:equivalentTo       $A\equiv B$      A equivalent_to B  A.equivalent_to.append(B)  A is equivalent to B  Class *equivalence*

                                                           B in A.equivalent_to                             Test for equivalence

owl:intersectionOf     $A\sqcap B$      A and B            A & B                      A and B               Class *intersection* (*conjunction*)

owl:unionOf            $A\sqcup B$      A or B             A | B                      A or B                Class *union* (*disjunction*)

owl:complementOf       $\lnot A$        not A              Not(A)                     not A                 Class *complement* (*negation*)

owl:oneOf              $\{a, b, ...\}$  {a, b, ...}        OneOf([a, b, ...])         one of a, b, ...      Class *enumeration*

rdf:type               $a:A$            a is_a A           a = A()                    a is a A              Class *assertion* (instantiation)

                                                           isinstance(a, A)                                 Test for instance of

owl:assertionProperty  $(a,b):R$        a object property  a.R.append(b)              a is R-related to b   Property *assertion*
                                        assertion b

owl:assertionProperty  $(a,n):R$        a data property    a.R.append(n)              a is R-related to n   Data *assertion*
                                        assertion n

owl:allValuesFrom      $\forall R.A$    R only A           R.only(A)                  all A with R          [*Universal restriction*][universal_restriction]

owl:someValuesFrom     $\exists R.A$    R some A           R.some(A)                  some A with R         [*Existential restriction*][existential_restriction]

owl:cardinality        $=n R.A$         R exactly n A      R.exactly(n, A)                                  *Cardinality restriction*

owl:minCardinality     $\leq n R.A$     R min n A          R.min(n, A)                                      *Minimum cardinality restriction*

owl:maxCardinality     $\geq n R.A$     R max n A          R.max(n, A)                                      *Minimum cardinality restriction*

owl:hasValue           $\exists R\{a\}$ R value a          R.value(a)                                       *Value restriction*

rdfs:domain            $\exists R.\top  R domain A         R.domain = [A]                                   Classes that the restriction applies to
                       \sqsubseteq A$

rdfs:range             $\top\sqsubseteq R range B          R.range = [B]                                    All classes that can be the value of the restriction
                       \forall R.B$

owl:inverseOf          $S\equiv R^-$    S inverse_of R     Inverse(R)                 S is inverse of R     Property *inverse*

                                                           S.inverse == R                                   Test for *inverse*

----------------------------------------------------------------------------------------------------------------------------------
