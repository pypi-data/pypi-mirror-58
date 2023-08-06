# Introduction

EMMO is a multidisciplinary effort to develop a standard
representational framework (the ontology) based on current materials
modelling knowledge, including physical sciences, analytical
philosophy and information and communication technologies.
This multidisciplinarity is illustrated by the figure on the title page.
It provides the connection between the physical world, materials
characterisation world and materials modelling world.

![EMMO provides the connection between the physical world, materials
characterisation world and materials modelling world.](figs/emmo-three_worlds.png){ width=620px }

EMMO is based on and is consistent with the [Review of Materials
Modelling][RoMM], [CEN Workshop Agreement][CWA] and [MODA
template][MODA].  However, while these efforts are written for humans,
EMMO is defined using the [Web Ontology Language (OWL)][OWL], which is
machine readable and allows for machine reasoning.  In terms of
semantic representation, EMMO brings everything to a much higher level.

As illustrated in the figure below, EMMO covers all aspects of
materials modelling and characterisation, including:

  - the **material** itself, which must be described in a rigorous way
  - the **observation process** involving an observer that percieves the
    real world
  - the **properties** that is measured or modelled
  - the **physics laws** that describes the material behaviour
  - the **physical models** that approximate the physics laws
  - the **solver** including the numerical discretisation method that
    leads to a solvable mathematical representation under certain
    simplifying assumptions
  - the **numerical solver** that performs the calculations
  - the **post processing** of experimental or simulated data

![The aspects of materials modelling and characterisation covered by EMMO.](figs/emmo-scope.png){ width=260px }

<!--
ADD MAIN FEATURES OF EMMO FROM GERHARDS SLIDE
-->



## What is an ontology
In short, an ontology is a specification of a conceptualization.  The
word *ontology* has a long history in philosophy, in which it refers
to the subject of existence.  The so-called [ontological
argument][ontological_argument] for the existence of God was proposed
by Anselm of Canterbury in 1078. He defined God as *"that than which
nothing greater can be thought"*, and argued that *"if the greatest
possible being exists in the mind, it must also exist in reality. If
it only exists in the mind, then an even greater being must be
possible -- one which exists both in the mind and in reality"*. Even
though this example has little to do with todays use of ontologies
in computer science, it illustrates the basic idea;  the ontology
defines some basic premises (concepts and relations between them) from
which it is possible reason to gain new knowledge.

For a more elaborated and modern definition of the ontology we refer
the reader to the one provided by [Tom Gruber (2009)][Gruber2009].
Another useful introduction to ontologies is the paper [Ontology
Development 101: A Guide to Creating Your First Ontology][Ontology101]
by Noy and McGuinness (2001), which is based on the [Protege][Protege]
sortware, with which EMMO has been developed.

A taxonomy is a hierarchical representation of classes and subclasses
connected via `is_a` relations.  Hence, it is a subset of the ontology
excluding all, but the `is_a` relations.  The main use of taxonomies
are for classifications.  The figure shows a simple example of a
taxonomy illustrating a categorisation of four classes into a
hierarchy of more higher of levels of generality.

![Example of a taxonomy.](figs/animal.png){ width=240px }

In EMMO is the taxonomy a rooted directed acyclic graph (DAG).  This
is an important since many classification methods relies on this
property, see e.g. [Valentini (2014)][Valentini2014] and [Robison et
al (2015)][Robison2015].  Note, that EMMO is a DAG does not prevent
some classes from having more than one parent.  A `quantitative_property`
is for instance both `formed` and an `objective_property`.  See
[appendix][Appendix] for the full EMMO taxonomy.


## Primitive elements in EMMO

![The primitive building blocks of EMMO.](figs/emmo-primitives.png){ width=620px }

### Individuals
Individuals are the basic, "ground level" components of EMMO.  They
may include concrete objects such as cars, flowers, stars, persons and
molecules, as well as abstract individuals such as a measured height,
a specific equation and software programs.

<!--
They are a logical picture of the real world entity they represent.

    Remove this for now, since Anne thinks this sentence no longer
    ahere to realism since we make a distinction between individuals
    and the real world.
-->

Individuals are not simple, but possess attributes in form of axioms
that are defined by the user (interpreter) upon declaration.


### Classes
Classes represents concepts.  They are the building blocks that we use
to create an ontology as a representation of knowledge.  We distinguish
between *defined* and *non-defined* classes.

Defined classes are defined by the requirements for being a member
of the class.  In the graphical representations of EMMO, defined
classes are orange.  For instance, in the graph of the top-level
entity branch below, `set` and `abstract` are defined classes.  `set`
is defined via the `has_member` relationship, while `abstract` is
defined via the `has_abstract_part` relationship.

Non-defined classes are defined as an abstract group of objects,
whos members are defined as belonging to the class.  They are yellow
in the graphical representations.

![Example of the top-level entity branch showing some classes and relationships between them.](figs/entity_branch.png){ width=246px }


### Axioms
Axioms are propositions in a logical framework that define the
relations between the individuals and classes.  They are used to
categorise individuals in classes and to define the *defined* classes.

The simplest form of a class axiom is a class description that just
states the existence of the class and gives it an unique identifier.
In order to provide more knowledge about the class, class axioms
typically contain additional components that state necessary
and/or sufficient characteristics of the class. OWL contains three
language constructs for combining class descriptions into class
axioms:

* `rdfs:subClassOf` allows one to say that the class extension of a
  class description is a subset of the class extension of another
  class description.

* `owl:equivalentClass` allows one to say that a class description has
  exactly the same class extension as another class description.

* `owl:disjointWith` allows one to say that the class extension of a
  class description has no members in common with the class extension
  of another class description.

See the section about [Description logic](#description-logic) for more
information about these language constructs.  Axioms are also used to
define relations between relations. These are further detailed in the
chapter on [Relations].




## Theoretical foundations
EMMO build upon several theoretical frameworks.

### Semiotics
Semiotics is the study of meaning-making.  It is the dicipline
of formulating something that possibly can exists in a defined
space and time in the real world. It is introdused in EMMO via the
`semion` class and used as a way to reduce the complexity of a
physical to a simple sign (symbol).  A `semion` is a physical
entity that represents an abstract object.

<!--
ADD FIGURE
-->


### Set theory
Set theory is the theory of membership. This is introduced via
the `set` class, representing the collection of all individuals
(signs) that represents a collection of items.  Sets are defined
via the `has_member` / `is_member_of` relations.


### Mereology
Mereology is the science of parthood.  It is introdused via
the `item` class and based on the mereological `has_part` /
`is_part_of` relations.

EMMO makes a strong distinction between membership and parthood
relations.  In contrast to sets, items can only have parts that
are themselves items.  This means for instance that parthood is
only between substrates of the same dimensionality.  Hence, the
boundary of an item is not a part of the item since it has a lower
dimensionality.

For further information, see [Casati and Varzi "Parts and Places" (1999)][Casati1999].


### Topology
Topology is the study of geometrical properties and spatial
(and time-wise) relations.  It is introdused in combination with
mereology (and therefore often referred to as **mereotopology**) via
the `substrate` class, which represents the place in space and
time in which every real world item exists.  Substrates in EMMO
are always topologically connedted in space and time.

Mereotopological relationships are defined with the `encloses` /
`is_enclosed_by` relations.


### Metrology
Metrology is the science of measurements.  It is used to
introduce units and link them to properties.


### Description logic
[Description logic (DL)][DL] is a formal knowledge representation language
in which the *axioms* are expressed.  It is less expressive than
[first-order logic (FOL)][FOL], but commonly used for providing the
logical formalism for ontologies and semantic web.  EMMO is expressed
in the [Web Ontology Language (OWL)][OWL], which is in turn is based
on DL.  This opens for features like reasoning.

Since it is essential to have a basic notion of OWL and DL, we
include here a very brief overview.  For a proper introduction to OWL
and DL, we refer the reader to sources like [Grau et.al. (2008)][Grau2008],
[OWL2 Primer][OWL2_Primer] and [OWL Reference][OWL_Reference].

OWL distinguishes six between types of class descriptions:

  1. a class identifier (a IRI reference)
  2. an exhaustive enumeration of individuals that together form the instances
     of a class (`owl:oneOf`)
  3. a property restriction (`owl:someValuesFrom`, `owl:allValuesFrom`,
     `owl:hasValue`, `owl:cardinality`, `owl:minCardinality`,
     `owl:maxCardinality`)
  4. the intersection of two or more class descriptions (`owl:intersectionOf`)
  5. the union of two or more class descriptions (`owl:unionOf`)
  6. the complement of a class description (`owl:complementOf`)

Except for the first, all of these refer to *defined classes*.  The
table below shows the notation in OWL, DL and the [Manchester OWL
syntax][Manchester_OWL], all commonly used for the definitions.  The
Manchester syntax is used by [Protege][Protege] and is designed to not
use DL symbols and to be easy and quick to read and write.  Several
other syntaxes exists for DL.  An interesting example is the pure
Python syntax proposed by [Lamy (2017)][Lamy2017], which is used in
the open source [Owlready2][Owlready2] Python package.

-----------------------------------------------------------------------------------------
OWL constructor    DL               Manchester        Read                 Meaning
---------------    ---------------- ----------------- -------------------  --------------
                   $A\doteq B$      ?                 A is defined to be   Class *definition*
                                                      equal to B

rdf:subclassOf     $A\sqsubseteq B$ A subclass_of B   all A are B          Class *inclusion*

owl:equivalentTo   $A\equiv B$      A equivalent_to B A is equivalent to B Class *equivalence*

owl:intersectionOf $A\sqcap B$      A and B           A and B              Class *intersection* (*conjunction*)

owl:unionOf        $A\sqcup B$      A or B            A or B               Class *union* (*disjunction*)

owl:complementOf   $\lnot A$        not A             not A                Class *complement* (*negation*)

owl:oneOf          $\{a, b, ...\}$  {a, b, ...}       one of a, b, ...     Class *enumeration*

rdf:type           $a:A$            a is_a A          a is a A             Class *assertion*

                   $(a,b):R$        a object property a is R-related to b  Property *assertion*
                                    assertion b

                   $(a,n):R$        a data property   a is R-related to n  Data *assertion*
                                    assertion n

                   $\top$           ?                 top                  A special class with every individual as an instance

                   $\bot$           ?                 bottom               The empty class

owl:allValuesFrom  $\forall R.A$    R only A          all A with R         [*Universal restriction*][universal_restriction]

owl:someValuesFrom $\exists R.A$    R some A          some A with R        [*Existential restriction*][existential_restriction]

owl:cardinality    $=n R.A$         R exactly n A                          *Cardinality restriction*

owl:minCardinality $\leq n R.A$     R min n A                              *Minimum cardinality restriction*

owl:maxCardinality $\geq n R.A$     R max n A                              *Minimum cardinality restriction*

owl:hasValue       $\exists R\{a\}$ R value a

rdfs:domain        $\exists R.\top  R domain A
                   \sqsubseteq A$

rdfs:range         $\top\sqsubseteq R range A
                   \forall R.A$

owl:inverseOf      $S\equiv R^-$    S inverse_of R    S is inverse of R    Property *inverse*

-----------------------------------------------------------------------------------------

Table: Notation for DL and Protege. A and B are classes, R is an active
relation, S is an passive relation, i and j are individuals and n is a
literal.

#### Examples
Here are some examples of different class descriptions using both
the DL and Manchester notation.

##### Inclusion (`rdf:subclassOf`)
Inclusion ($sqsubseteq$) defines necessary conditions. Necessary and
sufficient ($\equiv$) conditions defined with equivalence.

An employee is a person.

  **DL:** `employee` $sqsubseteq$ `person`

  **Manchester:** `employee is_a person`

##### Enumeration (`owl:oneOf`)
The color of a wine is either white, rose or red:

  **DL:** `wine_color` $\equiv$ {`white`, `rose`, `red`}

  **Manchester:** `wine_color equivalent_to {white, rose, red}`

##### Property restriction (`owl:someValuesFrom`)
A mother is a woman that has a child (some person):

  **DL:** `mother` $\equiv$ `woman` $\sqcap$ $\exists$`has_child`.`person`

  **Manchester:** `mother equivalent_to woman and has_child some person`

##### Property restriction (`owl:allValuesFrom`)
All parents that only have daughters:

  **DL:** `parents_with_only_daughters` $\equiv$ `person` $\sqcap$ $\forall$`has_child`.`woman`

  **Manchester:** `parents_with_only_daughters equivalent_to person and has_child only woman`

##### Property restriction (`owl:hasValue`)
The owl:hasValue restriction allows to define classes based on the
existence of particular property values. There must be at least one
matching property value.

All children of Mary:

  **DL:** `Marys_children` $\equiv$ `person` $\sqcap$ $\exists$`has_parent`.{`Mary`}

  **Manchester:** `Marys_children equivalent_to person and has_parent value Mary`

##### Property cardinality (`owl:cardinality`)
The owl:cardinality restriction allows to define classes based on the
maximum (owl:maxCardinality), minimum (owl:minCardinality) or exact
(owl:cardinality) number of occurences.

A person with one parent:

  **DL:** `half_orphant` $\equiv$ `person` and =1`has_parent`.`person`

  **Manchester:** `half_orphant equivalent_to person and has_parent exactly 1 person`

##### Intersection (`owl:intersectionOf`)
Individuals of the intersection of two classes, are simultaneously instances
of both classes.

A man is a person that is male:

  **DL:** `man` $\equiv$ `person` $\sqcap$ `male`

  **Manchester:** `man equivalent_to person and male`

##### Union (`owl:unionOf`)
Individuals of the union of two classes, are either instances
of one or both classes.

A person is a man or woman:

  **DL:** `person` $\equiv$ `man` $\sqcup$ `woman`

  **Manchester:** `person equivalent_to man or woman`

##### Complement (`owl:complementOf`)
Individuals of the complement of a class, are all individuals that are not
member of the class.

Not a man:

  **DL:** `female` $\equiv$ $\lnot$ `male`

  **Manchester:** `female equivalent_to not male`



## EMMO Structure

EMMO is structures in a hierarchical set of modules covering all
aspects materials modelling.  The modules and their interdependencies
are shows in the figure below.  Each module correspond to a separate
OWL file.  The special module `emmo-all.owl` includes all of EMMO.

![EMMO modules.](figs/emmo-structure.png){ width=400px }


### EMMO Core
EMMO core contains three levels as illustrated in the figure below.

![Toplevel structure of EMMO Core.](figs/emmo-core.png){ width=180px }

  - **The abstract conceptual level** makes a clear separation
    between `set` (set theory) and `item` (mereotopology).

  - **The geometric/topological level** contains the space (3D) and time
    (1D) in which all items unfolds.

  - **The physical level** holds the 4D `spacetime` in which all real
    world entities exists.  A `spacetime` that can be perceived by
    (interact with) the interpreater is a `physical`.  If the
    `spacetime` entity is empty in terms of perception, it is a
    `void`.

EMMO defines a parthood hierachy under `physical` by introducing the
following concepts (illustrated in the figure below):

  - **`elementary`** is the fundamental, non-divisible constituent of entities

  - **`state`** is a `physical`whose parts have a constant cardinality
    during its life time

  - **`existent`** is a succession of states

![Parthood hierachy under `physical`.](figs/physical.png){ width=500px }

Via the mereological direct parthood relation, EMMO can describe
entities made of parts at different levels of granularity.  This is
paramount for cross scale interoperability.  Every material in EMMO is
placed on a granularity level and the ontology gives information about
the direct upper and direct lower level classes using
the non-transitive direct parthood relations.

![Direct parthood.](figs/emmo-direct_part.png){ width=220px }


### EMMO Materials
EMMO Material contains a first draft of a materials ontology.  It
relies on direct parthood to identify granularity levels.  It is
generic and flexible enough to represent both classical and quantum
mechanical systems in a way that is compatible with different
interpretations (e.g. the Copenhagen and De Broglie-Bohm
interpretations of quantum mechanics) and levels of approximations
(e.g. classical physics and Born-Oppenheimer approximation).


### EMMO Semiotics

The semiotics module introduces three connected branches, `symbolic`,
`semiosis` and `semiotic_role` in addition to the
`has_sign`/`stands_for` family of relations.



Since the EMMO must represent models and properties (which are signs
that stand for a physical entity), the semiotic process must be
described also within the EMMO itself.  The concepts of Peirce
semiotics (interpreter, object, sign) are included in the semiotic
branch, together with the semiosis process.


### EMMO Formal languages




### EMMO Data formats

### EMMO Math

### EMMO Properties

### EMMO Models

### EMMO Characterisation



## How to read this document

### Annotations

All entities and relations in EMMO have some attributes, called
*annotations*.  In many cases, only the necessary *IRI* and *relations* are
provided.  However, more descriptive annotations, like *elucidation*
and *comment* will be added with time.  Possible annotations are:

<!--
- **Definition** is a human readable definition of the class.  Definition
  annotations are currently not used in EMMO.

- **Axiom**
  Currently not used in EMMO.

- **Theorem**
  Currently not used in EMMO.
-->

- **Elucidation** is a human readable explanation and clearification
  of the documented class or relation.

<!--
- **Domain**
  Currently not used in EMMO.

- **Range**
  Currently not used in EMMO.
-->

- **Example** clearifies the elucidation through an example.  A class may
  have several examples, each addressing different aspects.

- **Comment** is a clearifying note complementing the definition and
  elucidation.  A class may have several comments, each clearifying
  different aspects.

- **IRI** stands for *international resource identifier*.  It is an
  identifier that uniquely identifies the class or relation.  IRIs are
  similar to URIs, but are not restricted to the ASCII character set.
  Even though the IRIs used in EMMO appears to be URLs, they currently
  do not point to any existing content. This might change in the
  future.

- **Relations** is a list of relations applying to the current class
  or relation.  The relations for relations are special and will be
  elaborated on in the introduction to chapter [Relations].  Some of
  the listed relations are defined in the OWL sources, while other are
  inferred by the reasoner.

  The relations are using the Manchester OWL syntax introduced in section
  [Description logic](#description-logic).


### Graphs
The generated graphs borrows some syntax from the [Unified Modelling
Language (UML)][UML], which is a general purpose language for software
design and modelling.  The table below shows the style used for the
different types of relations and the concept they corresponds to in
UML.

Relation           UML arrow     UML concept
-------------      -----------   -----------
is-a               ![img][isa]   inheritance
disjoint_with      ![img][djw]   association
equivalent_to      ![img][eqt]   association
encloses           ![img][rel]   aggregation
has_abstract_part  ![img][rel]   aggregation
has_abstraction    ![img][rel]   aggregation
has_representation ![img][rel]   aggregation
has_member         ![img][rel]   aggregation
has_property       ![img][rel]   aggregation

Table: Notation for arrow styles used in the graphs.  Only active
relations are listed. Corresponding passive relations uses the same
style.

[isa]: figs/arrow-is_a.png "inheritance"
[djw]: figs/arrow-disjoint_with.png "association"
[eqt]: figs/arrow-equivalent_to.png "association"
[rel]: figs/arrow-relation.png "aggregation"


All relationships have a direction.  In the graphical visualisations,
the relationships are represented with an arrow pointing from the
subject to the object.  In order to reduce clutter and limit the size
of the graphs, the relations are abbreviated according to the
following table:

Relation                        Abbreviation
--------                        ------------
has_part only                   hp-o
is_part_of only                 ipo-o
has_member some                 hm-s
is_member_of some               imo-s
has_abstraction some            ha-s
is_abstraction_of some          iao-s
has_abstract_part only          pap-o
is_abstract_part_of only        iapo-o
has_space_slice some            hss-s
is_space_slice_of some          isso-s
has_time_slice some             hts-s
is_time_slice_of some           itso-s
has_projection some             hp-s
is_projection_of some           ipo-s
has_proper_part some            hpp-s
is_proper_part_of some          ippo-s
has_proper_part_of some         hppo-s
has_spatial_direct_part min     hsdp-m
has_spatial_direct_part some    hsdp-s
has_spatial_direct_part exactly hsdp-e

Table: Abbriviations of relations used in the graphical representation
of the different subbranches.


UML represents classes as a box with three compartment; name, attributes
and operators.  However, since the classes in EMMO have no operators and
it gives little meaning to include the OWL annotations as attributes,
we simply represent the classes as boxes.

As already mentioned, defined classes are colored orange, while
undefined classes are yellow.


<!--
## Further work

-->




[RoMM]: https://publications.europa.eu/en/publication-detail/-/publication/ec1455c3-d7ca-11e6-ad7c-01aa75ed71a1
[CWA]: https://www.cen.eu/news/workshops/Pages/WS_2016-013.aspx
[MODA]: https://emmc.info/moda-workflow-templates/
[ontological_argument]: https://en.wikipedia.org/wiki/Ontological_argument
[Valentini2014]: https://arxiv.org/abs/1406.4472
[Robison2015]: https://www.google.no/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0ahUKEwi_2vv-8tXbAhUFiiwKHVRdD4EQFgg1MAE&url=https%3A%2F%2Fwww.springer.com%2Fcda%2Fcontent%2Fdocument%2Fcda_downloaddocument%2F9783319202471-c2.pdf%3FSGWID%3D0-0-45-1510685-p177420182&usg=AOvVaw39c3v4a5PfVMEYDulWpF3w
[Gruber2009]: http://tomgruber.org/writing/ontology-definition-2007.htm
[Ontology101]: http://www.ksl.stanford.edu/people/dlm/papers/ontology-tutorial-noy-mcguinness-abstract.html
[DL]: https://en.wikipedia.org/wiki/Description_logic
[OWL]: https://en.wikipedia.org/wiki/Web_Ontology_Language
[FOL]: https://en.wikipedia.org/wiki/First-order_logic
[Casati1999]: https://mitpress.mit.edu/books/parts-and-places
[Grau2008]: http://www.cs.ox.ac.uk/boris.motik/pubs/ghmppss08next-steps.pdf
[OWL2_Primer]: https://www.w3.org/TR/owl2-primer/
[OWL_Reference]: https://www.w3.org/TR/owl-ref/
[Manchester_OWL]: http://ceur-ws.org/Vol-216/submission_9.pdf
[Owlready2]: https://pythonhosted.org/Owlready2/
[Lamy2017]: http://www.lesfleursdunormal.fr/_downloads/article_owlready_aim_2017.pdf
[universal_restriction]: https://en.wikipedia.org/wiki/Universal_quantifier
[existential_restriction]: https://en.wikipedia.org/wiki/Universal_quantifier
[Protege]: https://protege.stanford.edu/
[UML]: http://www.uml.org/



# EMMO relations
In the language of OWL, relations are called *properties*.  However,
since relations describe relations between classes and individuals and
since [properties](#Properties) has an other meaning in EMMO, we call
them *relations* here.

[Resource Description Framework (RDF)][RDF] is a W3C standard that is
widely used for describing informations on the web and is one of the
standards that OWL builds on.  RDF expresses information in form of
*subject-predicate-object* triplets.  The subject and object are
resources (aka items to describe) and the predicate expresses a
relationship between the subject and the object.

In EMMO, are the subject and object classes or individuals (or data)
while the predicate is a relation.  An example of an relationship is
the statement *dog is_a animal*.  Here is `dog` the subject, `is_a`
the predicate and `animal` the object.  We distinguish between
`active relations` where the subject is acting on the object and
`passive relations` where the subject is acted on by the object.

OWL distingues between `owl:ObjectProperty` that link classes or
individuals to classes or individuals and `owl:DatatypeProperty` that
links individuals to data values.  Since EMMO only deals with classes,
we will only be discussing object properties.  However, in actual
applications build on EMMO, datatype propertyes will be important.

The characteristics of the different properties is described by
the following *property axioms*:

- `rdf:subPropertyOf` is used to define that a property is a
  subproperty of some other property.  For instance, in the figure
  below showing the relation branch, we see that `active_relation` is
  a subproperty or `relation`.

  The `rdf:subPropertyOf` axioms forms a taxonomy-like tree for relations.

<!--
- `rdfs:domain` is not used in EMMO.

- `rdfs:range` is not used in EMMO.
-->

- `owl:equivalentProperty` states that two properties have the same
  property extension.

- `owl:inverseOf` axioms relate active relations to their corresponding
  passive relations, and vice versa. The root relation `relation` is its
  own inverse.

- `owl:FunctionalProperty` is a property that can have only one
  (unique) value y for each instance x, i.e. there cannot be two
  distinct values y1 and y2 such that the pairs (x,y1) and (x,y2) are
  both instances of this property. Both object properties and datatype
  properties can be declared as "functional".

- `owl:InverseFunctionalProperty`

- `owl:TransitiveProperty` states that if a pair (x,y) is an instance
  of P, and the pair (y,z) is also instance of P, then we can infer
  the the pair (x,z) is also an instance of P.

- `owl:SymmetricProperty` states that if the pair (x,y) is an instance of P,
  then the pair (y,x) is also an instance of P.

  A popular example of a symmetric property is the `friend_of` relation.




## emmo_relation branch


![The emmo_relation branch.](output/html_files/emmo_relation.pdf){ width=290px }



### emmo_relation

**Elucidation:** The sign that stand for the most generic EMMO relation.

**IRI:** [http://emmc.info/emmo-core#EMMO_ec2472ae_cf4a_46a5_8555_1556f5a6c3c5](http://emmc.info/emmo-core#EMMO_ec2472ae_cf4a_46a5_8555_1556f5a6c3c5)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:topObjectProperty
  - domain [emmo](#emmo)
  - range [emmo](#emmo)







## mereotopological branch


![The mereotopological branch.](output/html_files/mereotopological.pdf){ width=280px }



### mereotopological

**Elucidation:** The generic EMMO mereotopological relation.

**Comment:** Mereotopology merges mereological and topological concepts and provides relations between wholes, parts, boundaries, etc.

**IRI:** [http://emmc.info/emmo-core#EMMO_03212fd7_abfd_4828_9c8e_62c293052d4b](http://emmc.info/emmo-core#EMMO_03212fd7_abfd_4828_9c8e_62c293052d4b)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [emmo_relation](#emmo_relation)




### disconnected

**Elucidation:** The relation between two individuals that stand for real world topological disconnected objects.

**IRI:** [http://emmc.info/emmo-core#EMMO_517dfaf9_4970_41ac_81ee_d031627d2c7c](http://emmc.info/emmo-core#EMMO_517dfaf9_4970_41ac_81ee_d031627d2c7c)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:SymmetricProperty
  - is_a [mereotopological](#mereotopological)
  - Inverse(emmo-core.mereotopological)







## semiotic branch


![The semiotic branch.](output/html_files/semiotic.pdf){ width=499px }



### semiotic

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_2337e25c_3c60_43fc_a8f9_b11a3f974291](http://emmc.info/emmo-semiotics#EMMO_2337e25c_3c60_43fc_a8f9_b11a3f974291)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [emmo_relation](#emmo_relation)







## connected branch


![The connected branch.](output/html_files/connected.pdf){ width=342px }



### connected

**Definition:** Definition:
Cxy := x is connected with y

Axiom:
 1) Cxx (x is always connected with itself (reflexivity))
Axiom:
2) Cxy->Cyx (if x is connected with y then y is connected with x (symmetry))

**Elucidation:** The relation between two individuals that stand for real world topological connected objects.

**Comment:** Causality is a topological property between connected items.

**Comment:** Items being connected means that there is a topological contact or "interaction" between them.

**IRI:** [http://emmc.info/emmo-core#EMMO_6703954e_34c4_4a15_a9e7_f313760ae1a8](http://emmc.info/emmo-core#EMMO_6703954e_34c4_4a15_a9e7_f313760ae1a8)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:SymmetricProperty
  - is_a [mereotopological](#mereotopological)
  - Inverse(emmo-core.mereotopological)




### encloses

**IRI:** [http://emmc.info/emmo-core#EMMO_8c898653_1118_4682_9bbf_6cc334d16a99](http://emmc.info/emmo-core#EMMO_8c898653_1118_4682_9bbf_6cc334d16a99)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:TransitiveProperty
  - is_a [connected](#connected)
  - Inverse(emmo-core.connected)




### overlaps

**Definition:** Definition:
Oxy <=> ∃z(Pzx ∧ Pzy)

x overlap with y means that there exists a z that is part of both x and y

**IRI:** [http://emmc.info/emmo-core#EMMO_d893d373_b579_4867_841e_1c2b31a8d2c6](http://emmc.info/emmo-core#EMMO_d893d373_b579_4867_841e_1c2b31a8d2c6)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:SymmetricProperty
  - is_a [connected](#connected)
  - Inverse(emmo-core.connected)




### overcrosses

**IRI:** [http://emmc.info/emmo-core#EMMO_9cb984ca_48ad_4864_b09e_50d3fff19420](http://emmc.info/emmo-core#EMMO_9cb984ca_48ad_4864_b09e_50d3fff19420)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:SymmetricProperty
  - is_a [overlaps](#overlaps)
  - Inverse(emmo-core.overlaps)




### contacts

**IRI:** [http://emmc.info/emmo-core#EMMO_4d6504f1_c470_4ce9_b941_bbbebc9ab05d](http://emmc.info/emmo-core#EMMO_4d6504f1_c470_4ce9_b941_bbbebc9ab05d)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:SymmetricProperty
  - is_a [connected](#connected)
  - Inverse(emmo-core.connected)







## has_sign branch


![The has_sign branch.](output/html_files/has_sign.pdf){ width=384px }



### has_sign

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_60577dea_9019_4537_ac41_80b0fb563d41](http://emmc.info/emmo-semiotics#EMMO_60577dea_9019_4537_ac41_80b0fb563d41)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [semiotic](#semiotic)
  - domain [object](#object)
  - range [sign](#sign)




### has_convention

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_eb3518bf_f799_4f9e_8c3e_ce59af11453b](http://emmc.info/emmo-semiotics#EMMO_eb3518bf_f799_4f9e_8c3e_ce59af11453b)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_sign](#has_sign)
  - range [conventional](#conventional)




### has_variable

**IRI:** [http://emmc.info/emmo-math#EMMO_3446e167_c576_49d6_846c_215bb8878a55](http://emmc.info/emmo-math#EMMO_3446e167_c576_49d6_846c_215bb8878a55)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_convention](#has_convention)




### has_property

**IRI:** [http://emmc.info/emmo-properties#EMMO_e1097637_70d2_4895_973f_2396f04fa204](http://emmc.info/emmo-properties#EMMO_e1097637_70d2_4895_973f_2396f04fa204)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_convention](#has_convention)
  - range [property](#property)




### has_icon

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_39c3815d_8cae_4c8f_b2ff_eeba24bec455](http://emmc.info/emmo-semiotics#EMMO_39c3815d_8cae_4c8f_b2ff_eeba24bec455)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_sign](#has_sign)
  - range [icon](#icon)




### has_model

**IRI:** [http://emmc.info/emmo-models#EMMO_24c71baf_6db6_48b9_86c8_8c70cf36db0c](http://emmc.info/emmo-models#EMMO_24c71baf_6db6_48b9_86c8_8c70cf36db0c)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_icon](#has_icon)




### has_index

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_297999d6_c9e4_4262_9536_bd524d1c6e21](http://emmc.info/emmo-semiotics#EMMO_297999d6_c9e4_4262_9536_bd524d1c6e21)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_sign](#has_sign)
  - range [index](#index)







## has_part branch
[RDF]: https://en.wikipedia.org/wiki/Resource_Description_Framework

![The has_part branch.](output/html_files/has_part.pdf){ width=668px }



### has_part

**IRI:** [http://emmc.info/emmo-core#EMMO_17e27c22_37e1_468c_9dd7_95e137f73e7f](http://emmc.info/emmo-core#EMMO_17e27c22_37e1_468c_9dd7_95e137f73e7f)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:TransitiveProperty
  - is_a [encloses](#encloses)
  - is_a [overlaps](#overlaps)
  - Inverse(emmo-core.overlaps)




### has_proper_part

**IRI:** [http://emmc.info/emmo-core#EMMO_9380ab64_0363_4804_b13f_3a8a94119a76](http://emmc.info/emmo-core#EMMO_9380ab64_0363_4804_b13f_3a8a94119a76)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:TransitiveProperty
  - is_a [has_part](#has_part)




### has_spatial_part

**Elucidation:** A relation that isolates a proper part extending in time twithin the lifetime of the whole, without covering the full spatial extension of the 4D whole (i.e. is not a temporal part).

**IRI:** [http://emmc.info/emmo-4d#EMMO_f68030be_94b8_4c61_a161_886468558054](http://emmc.info/emmo-4d#EMMO_f68030be_94b8_4c61_a161_886468558054)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_proper_part](#has_proper_part)




### has_non_essential_part

**Elucidation:** A relation that isolates a proper part extending in time through a portion of the lifetime whole.

**IRI:** [http://emmc.info/emmo-4d#EMMO_6e046dd0_9634_4013_b2b1_9cc468087c83](http://emmc.info/emmo-4d#EMMO_6e046dd0_9634_4013_b2b1_9cc468087c83)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_spatial_part](#has_spatial_part)




### has_essential_part

**Elucidation:** A relation that isolates a proper part extending in time through all the lifetime of the whole.

**IRI:** [http://emmc.info/emmo-core#EMMO_42eef0b0_cc64_4380_b912_8cc37e87506c](http://emmc.info/emmo-core#EMMO_42eef0b0_cc64_4380_b912_8cc37e87506c)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:TransitiveProperty
  - is_a [has_spatial_part](#has_spatial_part)




### has_spatial_direct_part

**IRI:** [http://emmc.info/emmo-direct#EMMO_b2282816_b7a3_44c6_b2cb_3feff1ceb7fe](http://emmc.info/emmo-direct#EMMO_b2282816_b7a3_44c6_b2cb_3feff1ceb7fe)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:InverseFunctionalProperty
  - is_a owl:AsymmetricProperty
  - is_a owl:IrreflexiveProperty
  - is_a [has_essential_part](#has_essential_part)




### has_member

**IRI:** [http://emmc.info/emmo-core#EMMO_6b7276a4_4b9d_440a_b577_0277539c0fc4](http://emmc.info/emmo-core#EMMO_6b7276a4_4b9d_440a_b577_0277539c0fc4)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:AsymmetricProperty
  - is_a owl:IrreflexiveProperty
  - is_a [has_proper_part](#has_proper_part)
  - domain [collection](#collection)
  - range [item](#item)




### has_temporal_part

**Elucidation:** A relation that isolate a proper part that covers the total spatial extension of a whole within a time interval.elucidation

**IRI:** [http://emmc.info/emmo-core#EMMO_7afbed84_7593_4a23_bd88_9d9c6b04e8f6](http://emmc.info/emmo-core#EMMO_7afbed84_7593_4a23_bd88_9d9c6b04e8f6)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:TransitiveProperty
  - is_a [has_proper_part](#has_proper_part)




### has_temporal_direct_part

**IRI:** [http://emmc.info/emmo-direct#EMMO_65a2c5b8_e4d8_4a51_b2f8_e55effc0547d](http://emmc.info/emmo-direct#EMMO_65a2c5b8_e4d8_4a51_b2f8_e55effc0547d)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:InverseFunctionalProperty
  - is_a owl:AsymmetricProperty
  - is_a owl:IrreflexiveProperty
  - is_a [has_temporal_part](#has_temporal_part)




### has_direct_part

**IRI:** [http://emmc.info/emmo-direct#EMMO_a50d920d_1ee3_4668_9a73_5d80a1c6fe15](http://emmc.info/emmo-direct#EMMO_a50d920d_1ee3_4668_9a73_5d80a1c6fe15)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a owl:InverseFunctionalProperty
  - is_a owl:AsymmetricProperty
  - is_a owl:IrreflexiveProperty
  - is_a [has_proper_part](#has_proper_part)




### has_proper_participant

**IRI:** [http://emmc.info/emmo-process#EMMO_c5aae418_1622_4d02_93c5_21159e28e6c1](http://emmc.info/emmo-process#EMMO_c5aae418_1622_4d02_93c5_21159e28e6c1)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_proper_part](#has_proper_part)
  - is_a [has_participant](#has_participant)




### has_participant

**IRI:** [http://emmc.info/emmo-process#EMMO_ae2d1a96_bfa1_409a_a7d2_03d69e8a125a](http://emmc.info/emmo-process#EMMO_ae2d1a96_bfa1_409a_a7d2_03d69e8a125a)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_part](#has_part)
  - domain [process](#process)
  - range [participant](#participant)




### has_proper_participant

**IRI:** [http://emmc.info/emmo-process#EMMO_c5aae418_1622_4d02_93c5_21159e28e6c1](http://emmc.info/emmo-process#EMMO_c5aae418_1622_4d02_93c5_21159e28e6c1)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_proper_part](#has_proper_part)
  - is_a [has_participant](#has_participant)







# EMMO classes
*emmo* is a class representing the collection of all the individuals
(signs) that are used in the ontology. Individuals are declared by the
EMMO users when they want to apply the EMMO to represent the world.



## emmo branch
The root of all classes used to represent the world.  It has two children;
*collection* and *item*.

*collection* is the class representing the collection of all the
individuals (signs) that represents a collection of non-connected real world
objects.

*item* Is the class that collects all the individuals that are members
of a set (it's the most comprehensive set individual).  It is the
branch of parthood (mereotopology).






![The emmo branch.](output/html_files/emmo.pdf){ width=416px }



### emmo

**Elucidation:** The class representing the collection of all the individuals declared in this ontology that stand for real world objects.

**Comment:** 'emmo' is the disjoint union of 'item' and 'collection' (covering axiom).

The union implies that 'emmo' individuals can only be 'item' individuals (standing for self-connected real world objects) or 'collection' individuals (standing for a collection of disconnected items).

Disjointness means that a 'collection' individual cannot be an 'item' individual and viceversa, meaning that a real world object cannot be self-connected and non-self connected at the same time.

**Comment:** For the EMMO the universe is represented at meta-ontological level (i.e. the representational level that includes the ontologist, the ontology and the universe) as a 4D path-connected topological manifold (i.e. the spacetime).

A real world object is then a topological sub-region of the whole 4D manifold that describes our universe.

A universe sub-region is isolated and defined as a real world object by the ontologist, through a semiotic process that occurs on the meta-ontological level.

Mereotopology is the fundamental logical representation used to characterize the universe and to provide the definitions for the EMMO concepts.

The fundamental distinction between real world objects upon which the EMMO is based in self-connectedness: a real world object can be self-connected xor not self-connected.

**Comment:** In the EMMO we will refer to spacetime as a Minkowski space, restricting the ontology to special relativity only. However, exension to general relativity, will adding more complexity, should not change the overall approach.

**Comment:** Parthood relations does not change dimensionality of an 'emmo' individual, i.e. every part of a real world object always retains its 4D dimensionality.

It follows that, for the EMMO, real world objects of dimensionality lower than 4D do not exist (e.g. surfaces, lines).

**IRI:** [http://emmc.info/emmo-core#EMMO_802d3e92_8770_4f98_a289_ccaaab7fdddf](http://emmc.info/emmo-core#EMMO_802d3e92_8770_4f98_a289_ccaaab7fdddf)

**Relations:**

  - is_a owl:Thing




### collection

**Elucidation:** The class of all individuals that stands for a real world not self-connected object.

**Elucidation:** The class representing the collection of all the individuals (signs) that represents a collection of 'item' individuals.

**Comment:** A 'collection' individual is a sign that stands for a non-self-connected real world object.

A 'collection' individual is related to each 'item' individuals of the collection (i.e. the members) through the membership relation.

An 'item' individual stands for a real world self-connected object which can be represented as a whole made of connected parts (e.g. a car made of components).

**Comment:** A 'set' individual cannot be member of a 'set' (to avoid Russel's paradox).

**Comment:** Formally, 'set' is axiomatized as the class of individuals that 'has_member' some 'item'.

A 'set' cannot have as member another 'set'. This relation is expressed instead by the subset relation, which is the OWL-DL built-in 'is_a' relation used to declare subclasses of 'set'.

**Comment:** Since OWL-DL classes are intended as signs that stand for real world sets, we can consider the 'set' branch as a meta-ontological branch, since 'item' class and all its subclasses are then individuals of 'set'.

It is also possible to define a relation 'is_subset_of' valid only between 'set' individuals that is equivalent to the OWL-DL built-in 'is_a' relation between classes in the 'item' branch.

However this is not done in the EMMO for the sake of simplicity and due to the limitation of the language.

**Comment:** The 'set' class can be used to declare individuals that stand for collections of parts that does not form a self-connected whole in mereotopological sense.

e.g. the set of users of a particular software, the set of atoms that have been part of that just dissociated molecule, or even the set of atoms that are part of a molecule considered as single individual entities and not as a mereotopological self-connected fusion.

**IRI:** [http://emmc.info/emmo-core#EMMO_2d2ecd97_067f_4d0e_950c_d746b7700a31](http://emmc.info/emmo-core#EMMO_2d2ecd97_067f_4d0e_950c_d746b7700a31)

**Relations:**

  - is_a [emmo](#emmo)
  - ([has_member](#has_member) some [item](#item))




### item

**Elucidation:** The class of individuals that stand for single real world self-connected objects.

**Elucidation:** The class that collects all the individuals that are member of a set (it’s the most comprehensive set individual).

**Comment:** A real world object is self-connected if any two parts that make up the whole are connected to each other (here the concept of connection is primitive).

Alternatively, using the primitive path-connectivity concept we can define a self-connected real world object as an object for which each couple of points is path-connected.

**Comment:** An 'item' individual stands for a real world self-connected object which can be represented as a whole made of connected parts (e.g. a car made of components).

The 'item' individuals stand for sub-regions of the 4D spacetime.

In the EMMO, connectivity is the topological foundation of causality.

All physical systems, i.e. systems whose behaviour is explained by physics laws, are always represented by 'item'-s.

Members of a 'collection" lack of causality connection, i.e. they do not constitute a physical system.

**Comment:** The 'item' class and all its sub-classes are 'set' individuals.

The 'item' branch will be used to represent the world things and can be seen in practice as the ontology core.

**IRI:** [http://emmc.info/emmo-core#EMMO_eb3a768e_d53e_4be9_a23b_0714833c36de](http://emmc.info/emmo-core#EMMO_eb3a768e_d53e_4be9_a23b_0714833c36de)

**Relations:**

  - is_a [emmo](#emmo)




### quantum

**Elucidation:** An 'emmo' that can't be further divided in time nor in space.

**Comment:** A 'quantum' is the most fundamental subclass of 'item', since we consider it as the smallest self-connected 4D real world object.

The quantum concept recalls the fact that there is lower epistemological limit to our knowledge of the universe, related to the uncertainity principle.

**Comment:** A quantum is a 4D real world object.

**Comment:** A quantum is the EMMO mereological a-tomic entity.

To avoid confusion with the concept of atom coming from physics, we will use the expression quantum mereology, instead of atomistic mereology.

**IRI:** [http://emmc.info/emmo-core#EMMO_3f9ae00e_810c_4518_aec2_7200e424cf68](http://emmc.info/emmo-core#EMMO_3f9ae00e_810c_4518_aec2_7200e424cf68)

**Relations:**

  - is_a [item](#item)
  - ([has_proper_part](#has_proper_part) only owl:Nothing)




### void

**Definition:** A 'item' that has no 'physical' parts.

**IRI:** [http://emmc.info/emmo-core#EMMO_29072ec4_ffcb_42fb_bdc7_26f05a2e9873](http://emmc.info/emmo-core#EMMO_29072ec4_ffcb_42fb_bdc7_26f05a2e9873)

**Relations:**

  - is_a [item](#item)
  - ([has_part](#has_part) only [void](#void))




### existent

**Definition:** A 'item' which is a 'state' or made only of 'state' temporal direct parts.

**Comment:** 'existent' is the most important class to be used for representing real world objects under a reductionistic perspective (i.e. objects come from the composition of sub-part objects).

'existent' class collects all individuals that stand for real world objects that can be structured in temporal sub-parts of constant mereological cardinality (i.e. number of parts) through the temporal direct parthood, that provides a way to axiomatize tassellation principles for a specific whole class, and non-transitivity to retain the granularity levels.

e.g. a car, a supersaturated gas with nucleating nanoparticles, an atom that becomes ionized and then recombines with an electron.

**Comment:** IMPORTANT:
if we agree that every item can be partitioned in time into 'state'-s with constant cardinality, then 'existent' is conincident with 'item'.

**Comment:** ex-sistere (latin): to stay (to persist through time) outside others of the same type (to be distinct from the rest).

**IRI:** [http://emmc.info/emmo-direct#EMMO_52211e5e_d767_4812_845e_eb6b402c476a](http://emmc.info/emmo-direct#EMMO_52211e5e_d767_4812_845e_eb6b402c476a)

**Relations:**

  - is_a [physical](#physical)
  - is_a [item](#item)
  - is_a [state](#state) or ([has_temporal_direct_part](#has_temporal_direct_part) some [state](#state))
  - ([has_temporal_direct_part](#has_temporal_direct_part) only [state](#state))







## physical branch


![The physical branch.](output/html_files/physical.pdf){ width=374px }



### physical

**Elucidation:** A 'item' that is an 'elementary' or has some 'elementary' as proper parts and whose temporal proper parts are only 'physical'-s (i.e. it can be perceived without interruptions in time).

**Comment:** A 'physical' is the class that contains all the individuals that stand for real world objects that interact physically with the interpreter.

Perception is a subcategory of interaction.

A physical must be perceived through physical interaction by the ontologist. Then the ontologist can declare an individual standing for the physical object just perceived.

**Comment:** A 'physical' must include at least an 'elementary' part, but can also include void parts.

A 'physical' may include as part also the 'void' surrounding or enclosed by its 'physical' sub parts.

There are no particular criteria for 'physical'-s structure, except that is made of some 'elementary'-s as proper parts and not only 'void'.

This is done in order to:
a) take into account the quantum nature of physical systems, in which the actual position of sub-components (e.g. electrons in an atom) is not known except for its probability distribution function (according to the Copenhagen interpretation.)
b) take into account the fact that large entities (e.g. devices, cars, materials) have some void into them.

e.g. a 'spacetime' that has spatial parts an atom and a cubic light year of 'void' extending for some time can be a 'physical' individual.

**Comment:** A 'physical' with dimensions other than 4D cannot exist, following the restriction of the parent 'emmo' class.

It follows from the fact that perception is always a process (e.g. it unfolds in time).

e.g. you always have an aperture time when you take a picture or measure a property. Instantaneous perceptions are idealizations (abstractions) or a very small time measurement.

**Comment:** In the EMMO there are no relations such as 'occupies_space', since 'physical'-s are themselves the 4D region.

**Comment:** The EMMO can be used to represent real world entities as 'physical'-s that are easy to connect to classical or quantum mechanical based models.

Classical mechanics poses no representational issues, for the EMMO: the 4D representation of 'physical'-s is consistent with classical physics systems.

However, the representation of 'physical'-s that are typically analized through quantum mechanics (e.g. molecules, atoms, clusters), is not straightforward.

1) De Broglie - Bohm interpretation
The most simple approach is to rely on Bohmian mechanics, in which each particle is supposed to exists in a specific position between measurements (hidden variables approach), while its trajectory is calculated using a Guiding Equation based on a quantum field calculated with the Schroedinger Equation.

While this approach is really easy to implement in an ontology, since each entity has its own well defined 4D region, its mathematical representation failed to receive large consensus due to the difficulties to include relativistic effects, to be extended to subnuclear scale and the strong non-locality assumtpion of the quantum field.

Nevertheless, the Bohmian mechanics is a numerical approach that is used in electronic models to reduce the computational effort of the solution of Schroedinger Equation.

In practice, an EMMO user can declare a 'physical' individual that stand for the whole quantum system to be described, and at the same time all sub-parts individuals can be declared, having them a well defined position in time, according to De Broglie - Bohm interpretation. The Hamiltonian can be calculated by considering the sub-part individuals.

'physical'-s are then made of 'physical' parts and 'void' parts that stand for the space between 'physical'-s (e.g. the void between electrons and nucleus in an atom).

2) Copenhagen interpretation
In this interpretation the properties (e.g. energy level, position, spin) of a particle are not defined in the interval between two measurements and the quantum system is entangled (i.e. properties of particles in the sysyem are correlated) and described by a global wavefunction obtained solving the Schroedinger Equation.

Upon measurement, the wavefunction collapses to a combination of close eigenstates that provide information about bservables of the system components (e.g. position, energy).

The EMMO can be used to represent 'physical'-s that can be related to Copenhagen based models. In practice, the user should follow these steps:

a) define the quantum system as a 'physical' individual (e.g. an H2 molecule) under a specific class (e.g. 'h2_molecule'). This individual is the whole.

b) define the axioms of the  class that describe how many sub-parts are expected for the whole and their class types (e.g. 'h2_molecule' has axioms 'has_proper_part exactly 2 electron' and 'has_proper_part exactly 2 nucleus)

c) the user can now connect the whole to a Schroedinger equation based model whose Hamiltonian is calculated trough the information coming only from the axioms. No individuals are declared for the subparts!

d) a measurement done on the quantum system that provides information on the sub-part observables is interpreted as wavefunction collapse and leads to the end of the whole and the declaration of the sub-parts individuals which can be themselves other quantum systems

e.g. if the outer electron of the H2 molecule interacts with another entity defining its state, then the whole that stands for the entangled H2 molecule becomes a 'physical' made of an electron individual, a quantum system made of one electron and two nuclei and the void between them.

e.g. in the Born-Oppenheimer approximation the user represent the atom by un-entangling nucleus and electronic cloud. The un-entanglement comes in the form of declaration of individual as parts.

e.g. the double slit experiment can be represent in the EMMO as:
a) before the slit: a 'physical' that extend in space and has parts 'electron' and 'void', called 'single_electron_wave_function'. 'electron' and 'void' are only in the axioms and not decalred individuals.
b) during slit passage: a 'physical' made of one declared individual, the 'electron'.
c) after the slit: again 'single_electron_wave_function'
d) upon collision with the detector:  'physical' made of one declared individual, the 'electron'.

**Comment:** The purpose of the 'physical' branch is to provide a representation of the real world objects, while the models used to explain or predict the behaviour of the real world objects lay under the 'semiotic' branch.

More than one model can be connected to the same 'physical'.

e.g. Navier-Stokes or Euler equation applied to the same fluid

**IRI:** [http://emmc.info/emmo-core#EMMO_c5ddfdba_c074_4aa4_ad6b_1ac4942d300d](http://emmc.info/emmo-core#EMMO_c5ddfdba_c074_4aa4_ad6b_1ac4942d300d)

**Relations:**

  - is_a [item](#item)
  - is_a [elementary](#elementary) or ([has_proper_part](#has_proper_part) some [physical](#physical))
  - ([has_temporal_part](#has_temporal_part) only [physical](#physical))




### participant

**Elucidation:** A portion of a 'process' that participates to the 'process' with a specific role.

**Comment:** If we allow a void region to play a role in a process, the 'participant' class must belong to 'item'.

**Comment:** In the EMMO the relation of participation to a process falls under mereotopology.

**IRI:** [http://emmc.info/emmo-process#EMMO_49804605_c0fe_4538_abda_f70ba1dc8a5d](http://emmc.info/emmo-process#EMMO_49804605_c0fe_4538_abda_f70ba1dc8a5d)

**Relations:**

  - is_a [physical](#physical)




### semiotic

**Elucidation:** The class of semiotic elements used in Peirce's semiotic theory.

"Namely, a sign is something, A, which brings something, B, its interpretant sign determined or created by it, into the same sort of correspondence with something, C, its object, as that in which itself stands to C." (Peirce 1902, NEM 4, 20–21).

The triadic elements:
- 'sign': the sign A (e.g. a name)
- 'interpretant': the sign B as the effects of the sign A on the interpreter (e.g. the mental concept of what a name means)
- 'object': the object C (e.g. the entity to which the sign A and B refer to)

This class includes also the 'interpeter' i.e. the entity that connects the 'sign' to the 'object'

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_b803f122_4acb_4064_9d71_c1e5fd091fc9](http://emmc.info/emmo-semiotics#EMMO_b803f122_4acb_4064_9d71_c1e5fd091fc9)

**Relations:**

  - is_a [participant](#participant)
  - (Inverse(emmo-process.has_proper_participant) some [semiosis](#semiosis))
  - equivalent_to [interpreter](#interpreter) or [object](#object) or [sign](#sign)




### object

**Elucidation:** The object, in Peirce semiotics.

**Comment:** Here is assumed that the concept of 'object' is always relative to a 'semiotic' process. An 'object' does not exists per se, but it's always part of an interpretation.

The EMMO relies on strong reductionism, i.e. everything real is a formless collection of elementary particles: we give a meaning to real world entities only by giving them boundaries and defining them using 'sign'-s.

In this way the 'sign'-ed entity become and 'object', and the 'object' is the basic entity needed in order to apply a logical formalism to the real world entities (i.e. we can speak of it through its sign, and use logics on it through its sign).

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_6f5af708_f825_4feb_a0d1_a8d813d3022b](http://emmc.info/emmo-semiotics#EMMO_6f5af708_f825_4feb_a0d1_a8d813d3022b)

**Relations:**

  - is_a [semiotic](#semiotic)
  - equivalent_to ([has_sign](#has_sign) some [sign](#sign))




### interpreter

**Elucidation:** The entity (or agent, or observer, or cognitive entity) who connects 'sign', 'interpretant' and 'object'.

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_0527413c_b286_4e9c_b2d0_03fb2a038dee](http://emmc.info/emmo-semiotics#EMMO_0527413c_b286_4e9c_b2d0_03fb2a038dee)

**Relations:**

  - is_a [semiotic](#semiotic)
  - ([has_spatial_part](#has_spatial_part) some [interpretant](#interpretant))




### observer

**Elucidation:** An 'interpreter' that perceives another 'entity' (the 'object') through a specific perception mechanism and produces a 'property' (the 'sign') that stands for the result of that particular perception.

**IRI:** [http://emmc.info/emmo-properties#EMMO_1b52ee70_121e_4d8d_8419_3f97cd0bd89c](http://emmc.info/emmo-properties#EMMO_1b52ee70_121e_4d8d_8419_3f97cd0bd89c)

**Relations:**

  - is_a [interpreter](#interpreter)




### measurement_instrument

**IRI:** [http://emmc.info/emmo-physical-properties#EMMO_f2d5d3ad_2e00_417f_8849_686f3988d929](http://emmc.info/emmo-physical-properties#EMMO_f2d5d3ad_2e00_417f_8849_686f3988d929)

**Relations:**

  - is_a [observer](#observer)




### existent

**Definition:** A 'item' which is a 'state' or made only of 'state' temporal direct parts.

**Comment:** 'existent' is the most important class to be used for representing real world objects under a reductionistic perspective (i.e. objects come from the composition of sub-part objects).

'existent' class collects all individuals that stand for real world objects that can be structured in temporal sub-parts of constant mereological cardinality (i.e. number of parts) through the temporal direct parthood, that provides a way to axiomatize tassellation principles for a specific whole class, and non-transitivity to retain the granularity levels.

e.g. a car, a supersaturated gas with nucleating nanoparticles, an atom that becomes ionized and then recombines with an electron.

**Comment:** IMPORTANT:
if we agree that every item can be partitioned in time into 'state'-s with constant cardinality, then 'existent' is conincident with 'item'.

**Comment:** ex-sistere (latin): to stay (to persist through time) outside others of the same type (to be distinct from the rest).

**IRI:** [http://emmc.info/emmo-direct#EMMO_52211e5e_d767_4812_845e_eb6b402c476a](http://emmc.info/emmo-direct#EMMO_52211e5e_d767_4812_845e_eb6b402c476a)

**Relations:**

  - is_a [physical](#physical)
  - is_a [item](#item)
  - is_a [state](#state) or ([has_temporal_direct_part](#has_temporal_direct_part) some [state](#state))
  - ([has_temporal_direct_part](#has_temporal_direct_part) only [state](#state))




### vacuum

**IRI:** [http://emmc.info/emmo-material#EMMO_3c218fbe_60c9_4597_8bcf_41eb1773af1f](http://emmc.info/emmo-material#EMMO_3c218fbe_60c9_4597_8bcf_41eb1773af1f)

**Relations:**

  - is_a [physical](#physical)
  - equivalent_to [physical](#physical) and not ([has_part](#has_part) some [massive](#massive))




### field

**Elucidation:** A 'physical' with 'massless' parts that are mediators of interactions.

**IRI:** [http://emmc.info/emmo-material#EMMO_70dac51e_bddd_48c2_8a98_7d8395e91fc2](http://emmc.info/emmo-material#EMMO_70dac51e_bddd_48c2_8a98_7d8395e91fc2)

**Relations:**

  - is_a [physical](#physical)
  - equivalent_to ([has_part](#has_part) some [massless](#massless))







## process branch


![The process branch.](output/html_files/process.pdf){ width=587px }



### process

**Definition:** A 'process' is defined as a temporal part of a 'physical' that is categorized in a primitive process subclass according to what type of process we want to represent.

Following the common definition of process, every 'physical' is a process since every 4D object always has a time dimension. However, in the EMMO we restrict the meaning of the word process to 'physical'-s whose evolution in time have a particular meaning for the ontologist.

i.e. a 'process' is not only something that unfolds in time (which is automatically represented in a 4D ontology), but something happening that has a meaning for the interpreter.

**Elucidation:** A 'process' is always a 'physical', since a 'void' does not have elements that evolves in time.

However, 'void' parts inside a 'process' can be a 'participant'.

**Elucidation:** A temporal part of a 'physical' that identifies a particular type of evolution in time.

**IRI:** [http://emmc.info/emmo-process#EMMO_43e9a05d_98af_41b4_92f6_00f79a09bfce](http://emmc.info/emmo-process#EMMO_43e9a05d_98af_41b4_92f6_00f79a09bfce)

**Relations:**

  - is_a [physical](#physical)
  - ([has_participant](#has_participant) some [participant](#participant))




### physical_phenomenon

**IRI:** [http://emmc.info/emmo-models#EMMO_314d0bd5_67ed_437e_a609_36d46147cea7](http://emmc.info/emmo-models#EMMO_314d0bd5_67ed_437e_a609_36d46147cea7)

**Relations:**

  - is_a [process](#process)




### semiosis

**Elucidation:** A 'process', that has participant an 'interpreter', that is aimed to produce a 'sign' representing another participant, the 'interpreted'.

**Example:** Me looking a cat and saying loud: "Cat!" -> the semiosis process

me -> interpreter
cat -> object (in Peirce semiotics)
the cat perceived by my mind -> interpretant
"Cat!" -> sign, the produced sign

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_008fd3b2_4013_451f_8827_52bceab11841](http://emmc.info/emmo-semiotics#EMMO_008fd3b2_4013_451f_8827_52bceab11841)

**Relations:**

  - is_a [process](#process)
  - ([has_participant](#has_participant) some [interpreter](#interpreter))
  - ([has_proper_participant](#has_proper_participant) some [object](#object))
  - ([has_proper_participant](#has_proper_participant) some [sign](#sign))




### observation

**Elucidation:** A 'semiosis' that involves an 'observer' that perceives another 'entity' (the 'object') through a specific perception mechanism and produces a 'property' (the 'sign') that stands for the result of that particular perception.

**IRI:** [http://emmc.info/emmo-properties#EMMO_10a5fd39_06aa_4648_9e70_f962a9cb2069](http://emmc.info/emmo-properties#EMMO_10a5fd39_06aa_4648_9e70_f962a9cb2069)

**Relations:**

  - is_a [semiosis](#semiosis)
  - ([has_participant](#has_participant) some [observer](#observer))




### experiment

**Elucidation:** An experiment is a process that is intended to replicate a physical phenomenon in a controlled environment.

**IRI:** [http://emmc.info/emmo-models#EMMO_22522299_4091_4d1f_82a2_3890492df6db](http://emmc.info/emmo-models#EMMO_22522299_4091_4d1f_82a2_3890492df6db)

**Relations:**

  - is_a [observation](#observation)
  - ([has_participant](#has_participant) some [physical_phenomenon](#physical_phenomenon))




### theorization

**Elucidation:** The 'semiosis' process of interpreting a 'physical' and provide a complec sign, 'theory' that stands for it and explain it to another interpreter.

**IRI:** [http://emmc.info/emmo-models#EMMO_6c739b1a_a774_4416_bb31_1961486fa9ed](http://emmc.info/emmo-models#EMMO_6c739b1a_a774_4416_bb31_1961486fa9ed)

**Relations:**

  - is_a [observation](#observation)




### measurement

**Elucidation:** An 'observation' that results in a quantitative comparison of a 'property' of an 'object' with a standard reference.

**IRI:** [http://emmc.info/emmo-physical-properties#EMMO_463bcfda_867b_41d9_a967_211d4d437cfb](http://emmc.info/emmo-physical-properties#EMMO_463bcfda_867b_41d9_a967_211d4d437cfb)

**Relations:**

  - is_a [observation](#observation)
  - ([has_participant](#has_participant) some [measurement_instrument](#measurement_instrument))







## semiotic branch


![The semiotic branch.](output/html_files/semiotic.pdf){ width=499px }



### semiotic

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_2337e25c_3c60_43fc_a8f9_b11a3f974291](http://emmc.info/emmo-semiotics#EMMO_2337e25c_3c60_43fc_a8f9_b11a3f974291)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [emmo_relation](#emmo_relation)




### has_sign

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_60577dea_9019_4537_ac41_80b0fb563d41](http://emmc.info/emmo-semiotics#EMMO_60577dea_9019_4537_ac41_80b0fb563d41)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [semiotic](#semiotic)
  - domain [object](#object)
  - range [sign](#sign)




### has_convention

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_eb3518bf_f799_4f9e_8c3e_ce59af11453b](http://emmc.info/emmo-semiotics#EMMO_eb3518bf_f799_4f9e_8c3e_ce59af11453b)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_sign](#has_sign)
  - range [conventional](#conventional)




### has_variable

**IRI:** [http://emmc.info/emmo-math#EMMO_3446e167_c576_49d6_846c_215bb8878a55](http://emmc.info/emmo-math#EMMO_3446e167_c576_49d6_846c_215bb8878a55)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_convention](#has_convention)




### has_property

**IRI:** [http://emmc.info/emmo-properties#EMMO_e1097637_70d2_4895_973f_2396f04fa204](http://emmc.info/emmo-properties#EMMO_e1097637_70d2_4895_973f_2396f04fa204)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_convention](#has_convention)
  - range [property](#property)




### has_icon

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_39c3815d_8cae_4c8f_b2ff_eeba24bec455](http://emmc.info/emmo-semiotics#EMMO_39c3815d_8cae_4c8f_b2ff_eeba24bec455)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_sign](#has_sign)
  - range [icon](#icon)




### has_model

**IRI:** [http://emmc.info/emmo-models#EMMO_24c71baf_6db6_48b9_86c8_8c70cf36db0c](http://emmc.info/emmo-models#EMMO_24c71baf_6db6_48b9_86c8_8c70cf36db0c)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_icon](#has_icon)




### has_index

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_297999d6_c9e4_4262_9536_bd524d1c6e21](http://emmc.info/emmo-semiotics#EMMO_297999d6_c9e4_4262_9536_bd524d1c6e21)

**Relations:**

  - is_a owl:ObjectProperty
  - is_a [has_sign](#has_sign)
  - range [index](#index)







## state branch


![The state branch.](output/html_files/state.pdf){ width=668px }



### state

**Elucidation:** A 'physical' whose spatial direct parts extends from one change in spatial direct part cardinality (i.e. the number of spatial direct parts) to the immidiate next change.

**Example:** e.g. the existent in my glass is declared at t = t_start as made of two direct parts: the ice and the water. It will continue to exists as state as long as the ice is completely melt at t = t_end. The new state will be completely made of water. Between t_start and t_end there is an exchange of molecules between the ice and the water, but this does not affect the existence of the two states.

If we partition the existent in my glass as ice surrounded by several molecules (we do not use the object water as direct part) then the appearance of a molecule coming from the ice will cause a state to end and another state to begin.

**Comment:** Direct partitions declaration is a choice of the ontology developer that choses the classes to be used as direct parts, according to its own world view.

A 'state' can always be direct partitioned in 'elementary'-s and 'void' or 'physical'.

e.g. the water in my glass can be seen as a single object without declaring direct parts, or as made of H2O molecules direct parts.

**Comment:** The definition of 'state' implies that its direct parts (i.e. 'physicals') are not gained or lost during its temporal extension (they exist from the left to the right side of the time interval), so that the granularity of a 'state' is constant.

This does not mean that there cannot be a change in the internal structure of the 'state' direct parts. It means only that this change must not affect the existence of the direct part itself.

There is no change in granularity or cardinality of direct parts within a 'state'.

Also, the 'state' must cover all the time interval between two successive cardinality changes.

The use of spatial direct parthood in 'state' definition means that a 'state' cannot overlap in space another 'state'.

**Comment:** The usefulness of 'state' is that it makes it possible to describe the evolution in time of an 'existent' in terms of series of 'state'-s that can take into account the disappearance or appearance of parts within a 'physical'.

A 'state' is a recognizable granularity level of matter, in the sense that its direct parts do not appear or disappear within its lifetime as it can be for a generic 'existent'.

**Comment:** There is no change in granularity or cardinality of parts within a state.

The use of spatial direct parthood in state definition means that a state cannot overlap in space another state that is direct part of the same whole.

**IRI:** [http://emmc.info/emmo-direct#EMMO_36c79456_e29c_400d_8bd3_0eedddb82652](http://emmc.info/emmo-direct#EMMO_36c79456_e29c_400d_8bd3_0eedddb82652)

**Relations:**

  - is_a [existent](#existent)
  - is_a [quantum](#quantum) or ([has_spatial_direct_part](#has_spatial_direct_part) some [existent](#existent))




### elementary

**Elucidation:** The basic constituent of 'physical'-s that can be proper partitioned only in time up to quantum level.

**Comment:** 'elementary' is by definition the most simple example of 'state'.

**Comment:** According to mereology, this should be call 'a-tomistic' in the strict etimological sense of the word (from greek, a-tomos: un-divisible).

Mereology based on such items is called atomistic mereology.

However, in order not to confuse the lexicon between mereology and physics (in which an atom is a divisible physical entity) we prefer to call it 'elementary', recalling the concept of elementary particle coming from the standard particles model.

**IRI:** [http://emmc.info/emmo-core#EMMO_0f795e3e_c602_4577_9a43_d5a231aa1360](http://emmc.info/emmo-core#EMMO_0f795e3e_c602_4577_9a43_d5a231aa1360)

**Relations:**

  - is_a [subatomic](#subatomic)
  - is_a [state](#state)
  - is_a [quantum](#quantum) or ([has_temporal_part](#has_temporal_part) only [elementary](#elementary))




### massive

**IRI:** [http://emmc.info/emmo-material#EMMO_385b8f6e_43ac_4596_ad76_ac322c68b7ca](http://emmc.info/emmo-material#EMMO_385b8f6e_43ac_4596_ad76_ac322c68b7ca)

**Relations:**

  - is_a [elementary](#elementary)




### electron

**IRI:** [http://emmc.info/emmo-material#EMMO_8043d3c6_a4c1_4089_ba34_9744e28e5b3d](http://emmc.info/emmo-material#EMMO_8043d3c6_a4c1_4089_ba34_9744e28e5b3d)

**Relations:**

  - is_a [massive](#massive)




### quark

**IRI:** [http://emmc.info/emmo-material#EMMO_72d53756_7fb1_46ed_980f_83f47efbe105](http://emmc.info/emmo-material#EMMO_72d53756_7fb1_46ed_980f_83f47efbe105)

**Relations:**

  - is_a [massive](#massive)




### massless

**IRI:** [http://emmc.info/emmo-material#EMMO_e5488299_8dab_4ebb_900a_26d2abed8396](http://emmc.info/emmo-material#EMMO_e5488299_8dab_4ebb_900a_26d2abed8396)

**Relations:**

  - is_a [elementary](#elementary)




### photon

**IRI:** [http://emmc.info/emmo-material#EMMO_25f8b804_9a0b_4387_a3e7_b35bce5365ee](http://emmc.info/emmo-material#EMMO_25f8b804_9a0b_4387_a3e7_b35bce5365ee)

**Relations:**

  - is_a [massless](#massless)




### gluon

**IRI:** [http://emmc.info/emmo-material#EMMO_7db59e56_f68b_48b7_ae99_891c35ae5c3b](http://emmc.info/emmo-material#EMMO_7db59e56_f68b_48b7_ae99_891c35ae5c3b)

**Relations:**

  - is_a [massless](#massless)




### graviton

**IRI:** [http://emmc.info/emmo-material#EMMO_eb3c61f0_3983_4346_a0c6_e7f6b90a67a8](http://emmc.info/emmo-material#EMMO_eb3c61f0_3983_4346_a0c6_e7f6b90a67a8)

**Relations:**

  - is_a [massless](#massless)




### subatomic

**IRI:** [http://emmc.info/emmo-material#EMMO_7d66bde4_b68d_41cc_b5fc_6fd98c5e2ff0](http://emmc.info/emmo-material#EMMO_7d66bde4_b68d_41cc_b5fc_6fd98c5e2ff0)

**Relations:**

  - is_a [state](#state)




### elementary

**Elucidation:** The basic constituent of 'physical'-s that can be proper partitioned only in time up to quantum level.

**Comment:** 'elementary' is by definition the most simple example of 'state'.

**Comment:** According to mereology, this should be call 'a-tomistic' in the strict etimological sense of the word (from greek, a-tomos: un-divisible).

Mereology based on such items is called atomistic mereology.

However, in order not to confuse the lexicon between mereology and physics (in which an atom is a divisible physical entity) we prefer to call it 'elementary', recalling the concept of elementary particle coming from the standard particles model.

**IRI:** [http://emmc.info/emmo-core#EMMO_0f795e3e_c602_4577_9a43_d5a231aa1360](http://emmc.info/emmo-core#EMMO_0f795e3e_c602_4577_9a43_d5a231aa1360)

**Relations:**

  - is_a [subatomic](#subatomic)
  - is_a [state](#state)
  - is_a [quantum](#quantum) or ([has_temporal_part](#has_temporal_part) only [elementary](#elementary))




### massive

**IRI:** [http://emmc.info/emmo-material#EMMO_385b8f6e_43ac_4596_ad76_ac322c68b7ca](http://emmc.info/emmo-material#EMMO_385b8f6e_43ac_4596_ad76_ac322c68b7ca)

**Relations:**

  - is_a [elementary](#elementary)




### electron

**IRI:** [http://emmc.info/emmo-material#EMMO_8043d3c6_a4c1_4089_ba34_9744e28e5b3d](http://emmc.info/emmo-material#EMMO_8043d3c6_a4c1_4089_ba34_9744e28e5b3d)

**Relations:**

  - is_a [massive](#massive)




### quark

**IRI:** [http://emmc.info/emmo-material#EMMO_72d53756_7fb1_46ed_980f_83f47efbe105](http://emmc.info/emmo-material#EMMO_72d53756_7fb1_46ed_980f_83f47efbe105)

**Relations:**

  - is_a [massive](#massive)




### massless

**IRI:** [http://emmc.info/emmo-material#EMMO_e5488299_8dab_4ebb_900a_26d2abed8396](http://emmc.info/emmo-material#EMMO_e5488299_8dab_4ebb_900a_26d2abed8396)

**Relations:**

  - is_a [elementary](#elementary)




### photon

**IRI:** [http://emmc.info/emmo-material#EMMO_25f8b804_9a0b_4387_a3e7_b35bce5365ee](http://emmc.info/emmo-material#EMMO_25f8b804_9a0b_4387_a3e7_b35bce5365ee)

**Relations:**

  - is_a [massless](#massless)




### gluon

**IRI:** [http://emmc.info/emmo-material#EMMO_7db59e56_f68b_48b7_ae99_891c35ae5c3b](http://emmc.info/emmo-material#EMMO_7db59e56_f68b_48b7_ae99_891c35ae5c3b)

**Relations:**

  - is_a [massless](#massless)




### graviton

**IRI:** [http://emmc.info/emmo-material#EMMO_eb3c61f0_3983_4346_a0c6_e7f6b90a67a8](http://emmc.info/emmo-material#EMMO_eb3c61f0_3983_4346_a0c6_e7f6b90a67a8)

**Relations:**

  - is_a [massless](#massless)




### electron_cloud

**Elucidation:** A 'spacetime' that stands for a quantum system made of electrons.

**IRI:** [http://emmc.info/emmo-material#EMMO_1067b97a_84f8_4d22_8ace_b842b8ce355c](http://emmc.info/emmo-material#EMMO_1067b97a_84f8_4d22_8ace_b842b8ce355c)

**Relations:**

  - is_a [matter](#matter)
  - is_a [subatomic](#subatomic)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [electron](#electron))




### nucleon

**IRI:** [http://emmc.info/emmo-material#EMMO_50781fd9_a9e4_46ad_b7be_4500371d188d](http://emmc.info/emmo-material#EMMO_50781fd9_a9e4_46ad_b7be_4500371d188d)

**Relations:**

  - is_a [matter](#matter)
  - is_a [subatomic](#subatomic)




### proton

**IRI:** [http://emmc.info/emmo-material#EMMO_8f87e700_99a8_4427_8ffb_e493de05c217](http://emmc.info/emmo-material#EMMO_8f87e700_99a8_4427_8ffb_e493de05c217)

**Relations:**

  - is_a [nucleon](#nucleon)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [quark](#quark))




### neutron

**IRI:** [http://emmc.info/emmo-material#EMMO_df808271_df91_4f27_ba59_fa423c51896c](http://emmc.info/emmo-material#EMMO_df808271_df91_4f27_ba59_fa423c51896c)

**Relations:**

  - is_a [nucleon](#nucleon)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [quark](#quark))




### nucleus

**IRI:** [http://emmc.info/emmo-material#EMMO_f835f4d4_c665_403d_ab25_dca5cc74be52](http://emmc.info/emmo-material#EMMO_f835f4d4_c665_403d_ab25_dca5cc74be52)

**Relations:**

  - is_a [matter](#matter)
  - is_a [subatomic](#subatomic)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [nucleon](#nucleon))
  - ([has_spatial_direct_part](#has_spatial_direct_part) min 1 [proton](#proton))




### mesoscopic

**IRI:** [http://emmc.info/emmo-material#EMMO_174cf221_9d16_427c_abea_e217a948969b](http://emmc.info/emmo-material#EMMO_174cf221_9d16_427c_abea_e217a948969b)

**Relations:**

  - is_a [state](#state)




### molecule

**Elucidation:** An atom_based state defined by an exact number of e-bonded atomic species and an electron cloud made of the shared electrons.

**Example:** H20, C6H12O6, CH4

**Comment:** An entity is called essential if removing one direct part will lead to a change in entity class.

An entity is called redundand if removing one direct part will not lead to a change in entity class.

**Comment:** This definition states that this object is a non-periodic set of atoms or a set with a finite periodicity.

Removing an atom from the state will result in another type of atom_based state.

e.g. you cannot remove H from H20 without changing the molecule type (essential). However, you can remove a C from a nanotube (redundant). C60 fullerene is a molecule, since it has a finite periodicity and is made of a well defined number of atoms (essential). A C nanotube is not a molecule, since it has an infinite periodicity (redundant).

**IRI:** [http://emmc.info/emmo-material#EMMO_3397f270_dfc1_4500_8f6f_4d0d85ac5f71](http://emmc.info/emmo-material#EMMO_3397f270_dfc1_4500_8f6f_4d0d85ac5f71)

**Relations:**

  - is_a [mesoscopic](#mesoscopic)
  - is_a [matter](#matter)
  - ([has_spatial_direct_part](#has_spatial_direct_part) min 2 [e-bonded_atom](#e-bonded_atom))
  - ([has_spatial_direct_part](#has_spatial_direct_part) exactly 1 [electron_cloud](#electron_cloud))




### atomic

**IRI:** [http://emmc.info/emmo-material#EMMO_5c4aff3c_c30c_4507_86d5_b4df41eb9f2f](http://emmc.info/emmo-material#EMMO_5c4aff3c_c30c_4507_86d5_b4df41eb9f2f)

**Relations:**

  - is_a [state](#state)




### atom

**Elucidation:** An 'atom' is a 'nucleus' surrounded by an 'electron_cloud', i.e. a quantum system made of one or more bounded electrons.

**Example:** A standalone atom has direct part one 'nucleus' and one 'electron_cloud'.

An O 'atom' within an O2 'molecule' is an 'e-bonded_atom'.

In this material branch, H atom is a particular case, with respect to higher atomic number atoms, since as soon as it shares its electron it has no nucleus entangled electron cloud.

We cannot say that H2 molecule has direct part two H atoms, but has direct part two H nucleus.

**IRI:** [http://emmc.info/emmo-material#EMMO_eb77076b_a104_42ac_a065_798b2d2809ad](http://emmc.info/emmo-material#EMMO_eb77076b_a104_42ac_a065_798b2d2809ad)

**Relations:**

  - is_a [matter](#matter)
  - is_a [atomic](#atomic)
  - ([has_spatial_direct_part](#has_spatial_direct_part) exactly 1 [electron_cloud](#electron_cloud))
  - ([has_spatial_direct_part](#has_spatial_direct_part) exactly 1 [nucleus](#nucleus))




### standalone_atom

**Elucidation:** An atom that does not share electrons with other atoms.

**Comment:** A standalone atom can be bonded with other atoms by intermolecular forces (i.e. dipole–dipole, London dispersion force, hydrogen bonding), since this bonds does not involve electron sharing.

**IRI:** [http://emmc.info/emmo-material#EMMO_2fd3f574_5e93_47fe_afca_ed80b0a21ab4](http://emmc.info/emmo-material#EMMO_2fd3f574_5e93_47fe_afca_ed80b0a21ab4)

**Relations:**

  - is_a [atom](#atom)




### neutral_atom

**Elucidation:** A standalone atom that has no net charge.

**IRI:** [http://emmc.info/emmo-material#EMMO_4588526f_8553_4f4d_aa73_a483e88d599b](http://emmc.info/emmo-material#EMMO_4588526f_8553_4f4d_aa73_a483e88d599b)

**Relations:**

  - is_a [standalone_atom](#standalone_atom)




### ion_atom

**Elucidation:** A standalone atom with an unbalanced number of electrons with respect to its atomic number.

**Comment:** The ion_atom is the basic part of a pure ionic bonded compound i.e. without eclectron sharing,

**IRI:** [http://emmc.info/emmo-material#EMMO_db03061b_db31_4132_a47a_6a634846578b](http://emmc.info/emmo-material#EMMO_db03061b_db31_4132_a47a_6a634846578b)

**Relations:**

  - is_a [standalone_atom](#standalone_atom)




### e-bonded_atom

**Elucidation:** An electronic bonded atom that shares at least one electron to the atom_based entity of which is part of.

**Comment:** A real bond between atoms is always something hybrid between covalent, metallic and ionic.

In general, metallic and ionic bonds have atoms sharing electrons.

**Comment:** The bond types that are covered by this definition are the strong electonic bonds: covalent, metallic and ionic.

**Comment:** This class can be used to represent molecules as simplified quantum systems, in which outer molecule shared electrons are un-entangled with the inner shells of the atoms composing the molecule.

**IRI:** [http://emmc.info/emmo-material#EMMO_8303a247_f9d9_4616_bdcd_f5cbd7b298e3](http://emmc.info/emmo-material#EMMO_8303a247_f9d9_4616_bdcd_f5cbd7b298e3)

**Relations:**

  - is_a [atom](#atom)




### continuum

**Elucidation:** A state that is a collection of sufficiently large number of other parts such that:
- it is the bearer of qualities that can exists only by the fact that it is a sum of parts
- the smallest partition dV of the state volume in which we are interested in, contains enough parts to be statistically consistent: n [#/m3] x dV [m3] >> 1

**Comment:** A continuum is made of a sufficient number of parts that it continues to exists as continuum individual even after the loss of one of them i.e. a continuum is a redundant.

**Comment:** A continuum is not necessarily small (i.e. composed by the minimum amount of sates to fulfill the definition).

A single continuum individual can be the whole fluid in a pipe.

**Comment:** A continuum is the bearer of properties that are generated by the interactions of parts such as viscosity and thermal or electrical conductivity.

**IRI:** [http://emmc.info/emmo-material#EMMO_8b0923ab_b500_477b_9ce9_8b3a3e4dc4f2](http://emmc.info/emmo-material#EMMO_8b0923ab_b500_477b_9ce9_8b3a3e4dc4f2)

**Relations:**

  - is_a [state](#state)




### fluid

**Elucidation:** A continuum that has no fixed shape and yields easily to external pressure.

**Example:** Gas, liquid, plasma,

**IRI:** [http://emmc.info/emmo-material#EMMO_87ac88ff_8379_4f5a_8c7b_424a8fff1ee8](http://emmc.info/emmo-material#EMMO_87ac88ff_8379_4f5a_8c7b_424a8fff1ee8)

**Relations:**

  - is_a [continuum](#continuum)




### solid

**Elucidation:** A continuum characterized by structural rigidity and resistance to changes of shape or volume, that retains its shape and density when not confined.

**IRI:** [http://emmc.info/emmo-material#EMMO_a2b006f2_bbfd_4dba_bcaa_3fca20cd6be1](http://emmc.info/emmo-material#EMMO_a2b006f2_bbfd_4dba_bcaa_3fca20cd6be1)

**Relations:**

  - is_a [continuum](#continuum)







## matter branch


![The matter branch.](output/html_files/matter.pdf){ width=565px }



### matter

**Elucidation:** A 'physical' that possesses some 'massive' parts.

**IRI:** [http://emmc.info/emmo-material#EMMO_5b2222df_4da6_442f_8244_96e9e45887d1](http://emmc.info/emmo-material#EMMO_5b2222df_4da6_442f_8244_96e9e45887d1)

**Relations:**

  - is_a [physical](#physical)
  - equivalent_to ([has_part](#has_part) some [massive](#massive))




### electron_cloud

**Elucidation:** A 'spacetime' that stands for a quantum system made of electrons.

**IRI:** [http://emmc.info/emmo-material#EMMO_1067b97a_84f8_4d22_8ace_b842b8ce355c](http://emmc.info/emmo-material#EMMO_1067b97a_84f8_4d22_8ace_b842b8ce355c)

**Relations:**

  - is_a [matter](#matter)
  - is_a [subatomic](#subatomic)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [electron](#electron))




### atom

**Elucidation:** An 'atom' is a 'nucleus' surrounded by an 'electron_cloud', i.e. a quantum system made of one or more bounded electrons.

**Example:** A standalone atom has direct part one 'nucleus' and one 'electron_cloud'.

An O 'atom' within an O2 'molecule' is an 'e-bonded_atom'.

In this material branch, H atom is a particular case, with respect to higher atomic number atoms, since as soon as it shares its electron it has no nucleus entangled electron cloud.

We cannot say that H2 molecule has direct part two H atoms, but has direct part two H nucleus.

**IRI:** [http://emmc.info/emmo-material#EMMO_eb77076b_a104_42ac_a065_798b2d2809ad](http://emmc.info/emmo-material#EMMO_eb77076b_a104_42ac_a065_798b2d2809ad)

**Relations:**

  - is_a [matter](#matter)
  - is_a [atomic](#atomic)
  - ([has_spatial_direct_part](#has_spatial_direct_part) exactly 1 [electron_cloud](#electron_cloud))
  - ([has_spatial_direct_part](#has_spatial_direct_part) exactly 1 [nucleus](#nucleus))




### standalone_atom

**Elucidation:** An atom that does not share electrons with other atoms.

**Comment:** A standalone atom can be bonded with other atoms by intermolecular forces (i.e. dipole–dipole, London dispersion force, hydrogen bonding), since this bonds does not involve electron sharing.

**IRI:** [http://emmc.info/emmo-material#EMMO_2fd3f574_5e93_47fe_afca_ed80b0a21ab4](http://emmc.info/emmo-material#EMMO_2fd3f574_5e93_47fe_afca_ed80b0a21ab4)

**Relations:**

  - is_a [atom](#atom)




### neutral_atom

**Elucidation:** A standalone atom that has no net charge.

**IRI:** [http://emmc.info/emmo-material#EMMO_4588526f_8553_4f4d_aa73_a483e88d599b](http://emmc.info/emmo-material#EMMO_4588526f_8553_4f4d_aa73_a483e88d599b)

**Relations:**

  - is_a [standalone_atom](#standalone_atom)




### ion_atom

**Elucidation:** A standalone atom with an unbalanced number of electrons with respect to its atomic number.

**Comment:** The ion_atom is the basic part of a pure ionic bonded compound i.e. without eclectron sharing,

**IRI:** [http://emmc.info/emmo-material#EMMO_db03061b_db31_4132_a47a_6a634846578b](http://emmc.info/emmo-material#EMMO_db03061b_db31_4132_a47a_6a634846578b)

**Relations:**

  - is_a [standalone_atom](#standalone_atom)




### e-bonded_atom

**Elucidation:** An electronic bonded atom that shares at least one electron to the atom_based entity of which is part of.

**Comment:** A real bond between atoms is always something hybrid between covalent, metallic and ionic.

In general, metallic and ionic bonds have atoms sharing electrons.

**Comment:** The bond types that are covered by this definition are the strong electonic bonds: covalent, metallic and ionic.

**Comment:** This class can be used to represent molecules as simplified quantum systems, in which outer molecule shared electrons are un-entangled with the inner shells of the atoms composing the molecule.

**IRI:** [http://emmc.info/emmo-material#EMMO_8303a247_f9d9_4616_bdcd_f5cbd7b298e3](http://emmc.info/emmo-material#EMMO_8303a247_f9d9_4616_bdcd_f5cbd7b298e3)

**Relations:**

  - is_a [atom](#atom)




### molecule

**Elucidation:** An atom_based state defined by an exact number of e-bonded atomic species and an electron cloud made of the shared electrons.

**Example:** H20, C6H12O6, CH4

**Comment:** An entity is called essential if removing one direct part will lead to a change in entity class.

An entity is called redundand if removing one direct part will not lead to a change in entity class.

**Comment:** This definition states that this object is a non-periodic set of atoms or a set with a finite periodicity.

Removing an atom from the state will result in another type of atom_based state.

e.g. you cannot remove H from H20 without changing the molecule type (essential). However, you can remove a C from a nanotube (redundant). C60 fullerene is a molecule, since it has a finite periodicity and is made of a well defined number of atoms (essential). A C nanotube is not a molecule, since it has an infinite periodicity (redundant).

**IRI:** [http://emmc.info/emmo-material#EMMO_3397f270_dfc1_4500_8f6f_4d0d85ac5f71](http://emmc.info/emmo-material#EMMO_3397f270_dfc1_4500_8f6f_4d0d85ac5f71)

**Relations:**

  - is_a [mesoscopic](#mesoscopic)
  - is_a [matter](#matter)
  - ([has_spatial_direct_part](#has_spatial_direct_part) min 2 [e-bonded_atom](#e-bonded_atom))
  - ([has_spatial_direct_part](#has_spatial_direct_part) exactly 1 [electron_cloud](#electron_cloud))




### nucleon

**IRI:** [http://emmc.info/emmo-material#EMMO_50781fd9_a9e4_46ad_b7be_4500371d188d](http://emmc.info/emmo-material#EMMO_50781fd9_a9e4_46ad_b7be_4500371d188d)

**Relations:**

  - is_a [matter](#matter)
  - is_a [subatomic](#subatomic)




### proton

**IRI:** [http://emmc.info/emmo-material#EMMO_8f87e700_99a8_4427_8ffb_e493de05c217](http://emmc.info/emmo-material#EMMO_8f87e700_99a8_4427_8ffb_e493de05c217)

**Relations:**

  - is_a [nucleon](#nucleon)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [quark](#quark))




### neutron

**IRI:** [http://emmc.info/emmo-material#EMMO_df808271_df91_4f27_ba59_fa423c51896c](http://emmc.info/emmo-material#EMMO_df808271_df91_4f27_ba59_fa423c51896c)

**Relations:**

  - is_a [nucleon](#nucleon)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [quark](#quark))




### nucleus

**IRI:** [http://emmc.info/emmo-material#EMMO_f835f4d4_c665_403d_ab25_dca5cc74be52](http://emmc.info/emmo-material#EMMO_f835f4d4_c665_403d_ab25_dca5cc74be52)

**Relations:**

  - is_a [matter](#matter)
  - is_a [subatomic](#subatomic)
  - ([has_spatial_direct_part](#has_spatial_direct_part) some [nucleon](#nucleon))
  - ([has_spatial_direct_part](#has_spatial_direct_part) min 1 [proton](#proton))







## sign branch


![The sign branch.](output/html_files/sign.pdf){ width=668px }



### sign

**Elucidation:** An 'spacetime' that is used as sign ("semeion" in greek) that stands for another 'spacetime' through an semiotic process.

**Example:** A novel is made of chapters, paragraphs, sentences, words and characters (in a direct parthood mereological hierarchy).

Each of them are 'sign'-s.

A character can be the a-tomistic 'sign' for the class of texts.

The horizontal segment in the character "A" is direct part of "A" but it is not a 'sign' itself.

For plain text we can propose the ASCII symbols, for math the fundamental math symbols.

**Comment:** A 'sign' can have temporal-direct-parts which are 'sign' themselves.

A 'sign' usually have 'sign' spatial direct parts only up to a certain elementary semiotic level, in which the part is only a 'physical' and no more a 'sign' (i.e. it stands for nothing). This elementary semiotic level is peculiar to each particular system of signs (e.g. text, painting).

Just like an 'elementary' in the 'physical' branch, each 'sign' branch should have an a-tomistic mereological part.

**Comment:** According to Peirce, 'sign' includes three subcategories:
- symbols: that stand for an object through convention
- indeces: that stand for an object due to causal continguity
- icon: that stand for an object due to similitudes e.g. in shape or composition

**Comment:** In a 4D ontology one could question if a 'sign' should be defined as a spatial direct part of a 'semiosis' i.e. a proper part of a 'semiosis' during all its existence.

e.g. one can say that an unread text is not a 'sign': it was a 'sign' during the 'semiosis' process in which it was written, but after that it is something else, until somebody read it again.

However, this is not the case for an ontology, since declaring an individual under the 'sign' class (a semiosis outside the EMMO, a meta-semiosis) is equivalent to say that for the ontologist (an interpreter outside the EMMO, a meta-interpreter) the real entity (an object outside the EMMO, a meta-object) is a 'sign'.

So the 'semiosis' process within the EMMO is about how other 'interpreter'-s deal with the 'sign'-s here declared.

**Comment:** It can be defined as the semiotic branch of the EMMO.

'sign' subclasses categorize the type of signs that are used to create representations/models of the real world entities.

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_b21a56ed_f969_4612_a6ec_cb7766f7f31d](http://emmc.info/emmo-semiotics#EMMO_b21a56ed_f969_4612_a6ec_cb7766f7f31d)

**Relations:**

  - is_a [semiotic](#semiotic)
  - ([has_temporal_part](#has_temporal_part) only [sign](#sign))
  - equivalent_to [index](#index) or [conventional](#conventional) or [icon](#icon)




### index

**Elucidation:** A 'sign' that stands for an 'objectì due to causal continguity.

**Example:** Smoke stands for a combustion process (a fire).

My facial expression stands for my emotional status.

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_0cd58641_824c_4851_907f_f4c3be76630c](http://emmc.info/emmo-semiotics#EMMO_0cd58641_824c_4851_907f_f4c3be76630c)

**Relations:**

  - is_a [sign](#sign)




### icon

**Elucidation:** A 'sign' that stands for an 'object' by resembling or imitating it, in shape or by sharing a similar logical structure.

**Example:** A picture that reproduces the aspect of a person.

An equation that reproduces the logical connection of the properties of a physical entity.

**Comment:** Three subtypes of icon are possible:

(a) the image, which depends on a simple quality (e.g. picture)

(b) the diagram, whose internal relations, mainly dyadic or so taken, represent by analogy the relations in something (e.g. math formula, geometric flowchart)

(c) the metaphor, which represents the representative character of a sign by representing a parallelism in something else

[Wikipedia]

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_d7788d1a_020d_4c78_85a1_13563fcec168](http://emmc.info/emmo-semiotics#EMMO_d7788d1a_020d_4c78_85a1_13563fcec168)

**Relations:**

  - is_a [sign](#sign)




### model

**Elucidation:** A 'sign' that not only stands for a 'physical' or a 'process', but it is also a simplified representation, aimed to assist calculations for its description or for predictions of its behaviour.

A 'model' represents a 'physical' or a 'process' by direct similitude (e.g. small scale replica) or by capturing in a logical framework the relations between its properties (e.g. mathematical model).

**Comment:** A 'model' prediction is always a prediction of the properties of an entity, since an entity is known by an interpreter only through perception.

**IRI:** [http://emmc.info/emmo-models#EMMO_939483b1_0148_43d1_8b35_851d2cd5d939](http://emmc.info/emmo-models#EMMO_939483b1_0148_43d1_8b35_851d2cd5d939)

**Relations:**

  - is_a [icon](#icon)
  - equivalent_to (Inverse(emmo-models.has_model) some [physical](#physical))




### mathematical_model

**IRI:** [http://emmc.info/emmo-models#EMMO_f7ed665b_c2e1_42bc_889b_6b42ed3a36f0](http://emmc.info/emmo-models#EMMO_f7ed665b_c2e1_42bc_889b_6b42ed3a36f0)

**Relations:**

  - is_a [mathematical](#mathematical)
  - is_a [model](#model)




### physics_based_model

**Elucidation:** A solvable set of one Physics Equation and one or more Materials Relations.

**IRI:** [http://emmc.info/emmo-models#EMMO_b29fd350_39aa_4af7_9459_3faa0544cba6](http://emmc.info/emmo-models#EMMO_b29fd350_39aa_4af7_9459_3faa0544cba6)

**Relations:**

  - is_a [mathematical_model](#mathematical_model)
  - ([has_spatial_part](#has_spatial_part) some [physics_equation](#physics_equation))
  - ([has_spatial_part](#has_spatial_part) some [material_relation](#material_relation))




### continuum_model

**IRI:** [http://emmc.info/emmo-models#EMMO_4456a5d2_16a6_4ee1_9a8e_5c75956b28ea](http://emmc.info/emmo-models#EMMO_4456a5d2_16a6_4ee1_9a8e_5c75956b28ea)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### mesoscopic_model

**IRI:** [http://emmc.info/emmo-models#EMMO_53935db0_af45_4426_b9e9_244a0d77db00](http://emmc.info/emmo-models#EMMO_53935db0_af45_4426_b9e9_244a0d77db00)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### electronic_model

**IRI:** [http://emmc.info/emmo-models#EMMO_6eca09be_17e9_445e_abc9_000aa61b7a11](http://emmc.info/emmo-models#EMMO_6eca09be_17e9_445e_abc9_000aa61b7a11)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### atomistic_model

**IRI:** [http://emmc.info/emmo-models#EMMO_84cadc45_6758_46f2_ba2a_5ead65c70213](http://emmc.info/emmo-models#EMMO_84cadc45_6758_46f2_ba2a_5ead65c70213)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### data_based_model

**Elucidation:** A computational model that uses data to create new insight into the behaviour of a system.

**IRI:** [http://emmc.info/emmo-models#EMMO_a4b14b83_9392_4a5f_a2e8_b2b58793f59b](http://emmc.info/emmo-models#EMMO_a4b14b83_9392_4a5f_a2e8_b2b58793f59b)

**Relations:**

  - is_a [mathematical_model](#mathematical_model)




### conventional

**Elucidation:** A 'sign' that stand for an 'object' through convention, norm or habit, without any resemblance to it.

**Comment:** In Peirce semiotics this kind of sign category is called symbol. However, since symbol is also used in formal languages, the name is changed in conventional.

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_35d2e130_6e01_41ed_94f7_00b333d46cf9](http://emmc.info/emmo-semiotics#EMMO_35d2e130_6e01_41ed_94f7_00b333d46cf9)

**Relations:**

  - is_a [sign](#sign)




### theory

**Elucidation:** A 'conventional' that stand for a 'physical'.

**Comment:** The 'theory' is e.g. a proposition, a book or a paper whose sub-symbols suggest in the mind of the interpreter an interpretant structure that can represent a 'physical'.

It is not an 'icon' (like a math equation), because it has no common resemblance or logical structure with the 'physical'.

In Peirce semiotics: legisign-symbol-argument

**IRI:** [http://emmc.info/emmo-models#EMMO_8d2d9374_ef3a_47e6_8595_6bc208e07519](http://emmc.info/emmo-models#EMMO_8d2d9374_ef3a_47e6_8595_6bc208e07519)

**Relations:**

  - is_a [conventional](#conventional)




### natural_law

**IRI:** [http://emmc.info/emmo-models#EMMO_db9a009e_f097_43f5_9520_6cbc07e7610b](http://emmc.info/emmo-models#EMMO_db9a009e_f097_43f5_9520_6cbc07e7610b)

**Relations:**

  - is_a [theory](#theory)




### physical_law

**IRI:** [http://emmc.info/emmo-models#EMMO_9c32fd69_f480_4130_83b3_fb25d9face14](http://emmc.info/emmo-models#EMMO_9c32fd69_f480_4130_83b3_fb25d9face14)

**Relations:**

  - is_a [natural_law](#natural_law)




### material_law

**IRI:** [http://emmc.info/emmo-models#EMMO_f19ff3b4_6bfe_4c41_a2b2_9affd39c140b](http://emmc.info/emmo-models#EMMO_f19ff3b4_6bfe_4c41_a2b2_9affd39c140b)

**Relations:**

  - is_a [natural_law](#natural_law)




### interpretant

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_054af807_85cd_4a13_8eba_119dfdaaf38b](http://emmc.info/emmo-semiotics#EMMO_054af807_85cd_4a13_8eba_119dfdaaf38b)

**Relations:**

  - is_a [sign](#sign)







## symbolic branch


![The symbolic branch.](output/html_files/symbolic.pdf){ width=195px }



### symbolic

**Elucidation:** A 'symbol' or a composition of 'symbol'-s.

**Example:** fe@è0
emmo
!5*a
cat

**Comment:** In formal languages it is called a string of symbols.

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_057e7d57_aff0_49de_911a_8861d85cef40](http://emmc.info/emmo-semiotics#EMMO_057e7d57_aff0_49de_911a_8861d85cef40)

**Relations:**

  - is_a [physical](#physical)
  - is_a [symbol](#symbol) or ([has_spatial_part](#has_spatial_part) some [symbol](#symbol))







## symbol branch


![The symbol branch.](output/html_files/symbol.pdf){ width=455px }



### symbol

**Elucidation:** The class of individuals that stand for an elementary mark of a specific symbolic code (alphabet).

**Example:** The class of letter "A" is the symbol as idea and the letter A is the mark.

**Comment:** Subclasses of 'symbol' are alphabets, in formal languages terminology.

**Comment:** Symbols of a formal language need not be symbols of anything. For instance there are logical constants which do not refer to any idea, but rather serve as a form of punctuation in the language (e.g. parentheses).

Symbols of a formal language must be capable of being specified without any reference to any interpretation of them.
(Wikipedia)

**Comment:** The class is the idea of the symbol, while the individual of that class stands for a specific mark (or token) of that idea.

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_a1083d0a_c1fb_471f_8e20_a98f881ad527](http://emmc.info/emmo-semiotics#EMMO_a1083d0a_c1fb_471f_8e20_a98f881ad527)

**Relations:**

  - is_a [symbolic](#symbolic)




### math_symbol

**Elucidation:** A 'symbol' that is part of standard mathematical formalism.

**IRI:** [http://emmc.info/emmo-math#EMMO_031d61af_6405_41de_8880_df2f85a53383](http://emmc.info/emmo-math#EMMO_031d61af_6405_41de_8880_df2f85a53383)

**Relations:**

  - is_a [symbol](#symbol)
  - ([has_spatial_part](#has_spatial_part) only not [mathematical](#mathematical))




### number

**IRI:** [http://emmc.info/emmo-math#EMMO_1a663927_3b68_4618_acd3_a8aa0d406329](http://emmc.info/emmo-math#EMMO_1a663927_3b68_4618_acd3_a8aa0d406329)

**Relations:**

  - is_a [math_symbol](#math_symbol)




### variable

**Comment:** A 'variable' is a 'symbol' that stands for a numerical defined 'mathematical' entity like e.g. a number, a vector, a matrix.

**IRI:** [http://emmc.info/emmo-math#EMMO_1eed0732_e3f1_4b2c_a9c4_b4e75eeb5895](http://emmc.info/emmo-math#EMMO_1eed0732_e3f1_4b2c_a9c4_b4e75eeb5895)

**Relations:**

  - is_a [math_symbol](#math_symbol)




### constant

**Elucidation:** A 'varaible' that stand for a well known constant.

**Comment:** pi = 3.14

**IRI:** [http://emmc.info/emmo-math#EMMO_ae15fb4f_8e4d_41de_a0f9_3997f89ba6a2](http://emmc.info/emmo-math#EMMO_ae15fb4f_8e4d_41de_a0f9_3997f89ba6a2)

**Relations:**

  - is_a [variable](#variable)




### parameter

**Example:** Viscosity, the total energy of the system given by an Hamiltonian, the force between two atoms.

**Comment:** A 'variable' whose value is assumed to be known independently from the equation, but whose value is not explicitated in the equation.

**IRI:** [http://emmc.info/emmo-math#EMMO_d1d436e7_72fc_49cd_863b_7bfb4ba5276a](http://emmc.info/emmo-math#EMMO_d1d436e7_72fc_49cd_863b_7bfb4ba5276a)

**Relations:**

  - is_a [variable](#variable)




### unknown

**Elucidation:** The dependent variable for which an equation has been written.

**Example:** Velocity, for the Navier-Stokes equation.

**IRI:** [http://emmc.info/emmo-math#EMMO_fe7e56ce_118b_4243_9aad_20eb9f4f31f6](http://emmc.info/emmo-math#EMMO_fe7e56ce_118b_4243_9aad_20eb9f4f31f6)

**Relations:**

  - is_a [variable](#variable)







## formula branch


![The formula branch.](output/html_files/formula.pdf){ width=273px }



### formula

**Elucidation:** A composition of 'symbol'-s respecting a specific language syntactic rules (well-formed formula).

**Example:** The word "cat" considered as a collection of 'symbol'-s respecting the rules of english language.

In this example the 'symbolic' entity "cat" is not related to the real cat, but it is only a word (like it would be to an italian person that ignores the meaning of this english word).

If an 'interpreter' skilled in english language is involved in a 'semiotic' process with this word, that "cat" became also a 'sign' i.e. it became for the 'interpreter' a representation for a real cat.

**Comment:** In formal languages the terms word or well-formed formula are used with the same meaning.

**IRI:** [http://emmc.info/emmo-semiotics#EMMO_50ea1ec5_f157_41b0_b46b_a9032f17ca10](http://emmc.info/emmo-semiotics#EMMO_50ea1ec5_f157_41b0_b46b_a9032f17ca10)

**Relations:**

  - is_a [symbolic](#symbolic)







## mathematical branch


![The mathematical branch.](output/html_files/mathematical.pdf){ width=668px }



### mathematical

**Comment:** The class of general mathematical symbols.

**IRI:** [http://emmc.info/emmo-math#EMMO_54ee6b5e_5261_44a8_86eb_5717e7fdb9d0](http://emmc.info/emmo-math#EMMO_54ee6b5e_5261_44a8_86eb_5717e7fdb9d0)

**Relations:**

  - is_a [formula](#formula)




### equation

**Comment:** The class of 'mathematical'-s that stand for a mathematical expression that puts in relation some variables and that can always be represented as:

f(v0, v1, ..., vn) = g(v0, v1, ..., vn)

where f is the left hand and g the right hand  side expressions and v0, v1, ..., vn are the variables.

e.g.

x^2 +3x  = 5x

dv/dt = a

sin(x) = y

**IRI:** [http://emmc.info/emmo-math#EMMO_e56ee3eb_7609_4ae1_8bed_51974f0960a6](http://emmc.info/emmo-math#EMMO_e56ee3eb_7609_4ae1_8bed_51974f0960a6)

**Relations:**

  - is_a [mathematical](#mathematical)
  - ([has_spatial_part](#has_spatial_part) some [variable](#variable))




### physics_equation

**Elucidation:** An 'equation' that stands for a 'physical_law' by mathematically defining the relations between physics_quantities.

**Comment:** The Newton's equation of motion.

The Schrodinger equation.

The Navier-Stokes equation.

**IRI:** [http://emmc.info/emmo-models#EMMO_27c5d8c6_8af7_4d63_beb1_ec37cd8b3fa3](http://emmc.info/emmo-models#EMMO_27c5d8c6_8af7_4d63_beb1_ec37cd8b3fa3)

**Relations:**

  - is_a [equation](#equation)
  - ([has_spatial_part](#has_spatial_part) some [physical_quantity](#physical_quantity))




### material_relation

**Elucidation:** An 'equation' that stands for a physical assumption specific to a material, and provides an expression for a 'physics_quantity' (the dependent variable) as function of other variables, physics_quantity or data (independent variables).

**Example:** The Lennard-Jones potential.

A force field.

An Hamiltonian.

**Comment:** A material_relation can e.g. return a predefined number, return a database query, be an equation that depends on other physics_quantities.

**IRI:** [http://emmc.info/emmo-models#EMMO_e5438930_04e7_4d42_ade5_3700d4a52ab7](http://emmc.info/emmo-models#EMMO_e5438930_04e7_4d42_ade5_3700d4a52ab7)

**Relations:**

  - is_a [equation](#equation)
  - ([has_spatial_part](#has_spatial_part) some [physical_quantity](#physical_quantity))




### mathematical_model

**IRI:** [http://emmc.info/emmo-models#EMMO_f7ed665b_c2e1_42bc_889b_6b42ed3a36f0](http://emmc.info/emmo-models#EMMO_f7ed665b_c2e1_42bc_889b_6b42ed3a36f0)

**Relations:**

  - is_a [mathematical](#mathematical)
  - is_a [model](#model)




### physics_based_model

**Elucidation:** A solvable set of one Physics Equation and one or more Materials Relations.

**IRI:** [http://emmc.info/emmo-models#EMMO_b29fd350_39aa_4af7_9459_3faa0544cba6](http://emmc.info/emmo-models#EMMO_b29fd350_39aa_4af7_9459_3faa0544cba6)

**Relations:**

  - is_a [mathematical_model](#mathematical_model)
  - ([has_spatial_part](#has_spatial_part) some [physics_equation](#physics_equation))
  - ([has_spatial_part](#has_spatial_part) some [material_relation](#material_relation))




### continuum_model

**IRI:** [http://emmc.info/emmo-models#EMMO_4456a5d2_16a6_4ee1_9a8e_5c75956b28ea](http://emmc.info/emmo-models#EMMO_4456a5d2_16a6_4ee1_9a8e_5c75956b28ea)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### mesoscopic_model

**IRI:** [http://emmc.info/emmo-models#EMMO_53935db0_af45_4426_b9e9_244a0d77db00](http://emmc.info/emmo-models#EMMO_53935db0_af45_4426_b9e9_244a0d77db00)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### electronic_model

**IRI:** [http://emmc.info/emmo-models#EMMO_6eca09be_17e9_445e_abc9_000aa61b7a11](http://emmc.info/emmo-models#EMMO_6eca09be_17e9_445e_abc9_000aa61b7a11)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### atomistic_model

**IRI:** [http://emmc.info/emmo-models#EMMO_84cadc45_6758_46f2_ba2a_5ead65c70213](http://emmc.info/emmo-models#EMMO_84cadc45_6758_46f2_ba2a_5ead65c70213)

**Relations:**

  - is_a [physics_based_model](#physics_based_model)




### data_based_model

**Elucidation:** A computational model that uses data to create new insight into the behaviour of a system.

**IRI:** [http://emmc.info/emmo-models#EMMO_a4b14b83_9392_4a5f_a2e8_b2b58793f59b](http://emmc.info/emmo-models#EMMO_a4b14b83_9392_4a5f_a2e8_b2b58793f59b)

**Relations:**

  - is_a [mathematical_model](#mathematical_model)







## quantitative_property branch


![The quantitative_property branch.](output/html_files/quantitative_property.pdf){ width=360px }



### quantitative_property

**Elucidation:** A 'property' that can be quantified with respect to a standardized reference physical instance (e.g. the prototype meter bar, the kg prototype) or method (e.g. resilience) through a measurement process.

**IRI:** [http://emmc.info/emmo-physical-properties#EMMO_dd4a7f3e_ef56_466c_ac1a_d2716b5f87ec](http://emmc.info/emmo-physical-properties#EMMO_dd4a7f3e_ef56_466c_ac1a_d2716b5f87ec)

**Relations:**

  - is_a [objective_property](#objective_property)
  - is_a [formula](#formula)




### physical_quantity

**Elucidation:** A "symbolic" entity that is made of a 'number' and a 'measurement_unit'.

By definition it also stands for the result of a measurement process, and so it is also a 'sign'.

**Comment:** Measured or simulated 'physical propertiy'-s are always defined by a physical law, connected to a physical entity through a model perspective and measurement is done according to the same model.

Systems of units suggests that this is the correct approach, since except for the fundamental units (length, time, charge) every other unit is derived by mathematical relations between these fundamental units, implying a physical laws or definitions.

**IRI:** [http://emmc.info/emmo-physical-properties#EMMO_02c0621e_a527_4790_8a0f_2bb51973c819](http://emmc.info/emmo-physical-properties#EMMO_02c0621e_a527_4790_8a0f_2bb51973c819)

**Relations:**

  - is_a [quantitative_property](#quantitative_property)
  - ([has_spatial_part](#has_spatial_part) some [number](#number))
  - ([has_spatial_part](#has_spatial_part) some [measurement_unit](#measurement_unit))




### measurement_unit

**Elucidation:** A 'quantitative_property' that stands for the standard reference magnitude of a specific class of measurement processes, defined and adopted by convention or by law.

Quantitative measurement results are expressed as a multiple of the 'measurement_unit'.

**IRI:** [http://emmc.info/emmo-physical-properties#EMMO_b081b346_7279_46ef_9a3d_2c088fcd79f4](http://emmc.info/emmo-physical-properties#EMMO_b081b346_7279_46ef_9a3d_2c088fcd79f4)

**Relations:**

  - is_a [quantitative_property](#quantitative_property)




### descriptive_property

**IRI:** [http://emmc.info/emmo-physical-properties#EMMO_c46f091c_0420_4c1a_af30_0a2c8ebcf7d7](http://emmc.info/emmo-physical-properties#EMMO_c46f091c_0420_4c1a_af30_0a2c8ebcf7d7)

**Relations:**

  - is_a [quantitative_property](#quantitative_property)







## property branch


![The property branch.](output/html_files/property.pdf){ width=470px }



### property

**Elucidation:** A 'sign' that stands for an 'object' that the 'interpreter' perceived through a well defined 'observation' process.

(a property is always a partial representation of an 'object' since it reflects the 'object' capability to be part of a specific 'observation' process)

**Example:** Hardness is a subclass of properties.

Vickers hardness is a subclass of hardness that involves the procedures and instruments defined by the standard hardness test.

**Example:** Let's define the class 'colour' as the subclass of the properties that involve photon emission and an electromagnetic radiation sensible observer.

An individual C of this class 'colour' can be defined be declaring the process individual (e.g. daylight illumination) and the observer (e.g. my eyes)

Stating that an entity E has_property C, we mean that it can be observed by such setup of process + observer (i.e. observed by my eyes under daylight).

This definition can be generalized by using a generic human eye, so that the observer can be a generic human.

This can be used in material characterization, to define exactly the type of measurement done, including the instrument type.

**Comment:** We know real world entities through observation/perception.

A non-perceivable real world entity does not exist (or it exists on a plane of existance that has no intersection with us and we can say nothing about it).

Perception/observation of a real wolrd entity occurs when the entity stimulate an observer in a peculiar way through a well defined perception channel.

For this reason each property is related to a specific observation process which involves a specific observer with its own perception mechanisms.

The observation process (e.g. a look, a photo shot, a measurement) is performed  by an observer (e.g. you, a camera, an instrument) through a specific perception mechanism (e.g. retina impression, CMOS excitation, piezoelectric sensor activation) and involves an observed entity.

An observation is a semiotic process, since it stimulate an interpretant within the interpreter who can communicate the perception result to other interpreters through a sign which is the property.

Property subclasses are specializations that depend on the type of observation processes.

e.g. the property 'colour' is related to a process that involves emission or interaction of photon and an observer who can perceive electromagnetic radiation in the visible frequency range.

Properties usually relies on symbolic systems (e.g. for colour it can be palette or RGB).

**IRI:** [http://emmc.info/emmo-properties#EMMO_b7bcff25_ffc3_474e_9ab5_01b1664bd4ba](http://emmc.info/emmo-properties#EMMO_b7bcff25_ffc3_474e_9ab5_01b1664bd4ba)

**Relations:**

  - is_a [symbolic](#symbolic)
  - is_a [conventional](#conventional)
  - (Inverse(emmo-properties.has_property) some [emmo](#emmo))




### objective_property

**Elucidation:** A 'property' that is determined by each 'observer' following a well defined 'observation' procedure through a specific perception channel.

**Comment:** The word objective does not mean that each observation will provide the same results. It means that the observation followed a well defined procedure.

**IRI:** [http://emmc.info/emmo-properties#EMMO_2a888cdf_ec4a_4ec5_af1c_0343372fc978](http://emmc.info/emmo-properties#EMMO_2a888cdf_ec4a_4ec5_af1c_0343372fc978)

**Relations:**

  - is_a [property](#property)




### qualitative_property

**Elucidation:** An 'objective_property' that cannot be quantified.

**Example:** CFC is a 'sign' that stands for the fact that the morphology of atoms composing the microstructure of an entity is predominantly Cubic Face Centered

**IRI:** [http://emmc.info/emmo-physical-properties#EMMO_909415d1_7c43_4d5e_bbeb_7e1910159f66](http://emmc.info/emmo-physical-properties#EMMO_909415d1_7c43_4d5e_bbeb_7e1910159f66)

**Relations:**

  - is_a [objective_property](#objective_property)




### subjective_property

**Elucidation:** A 'property' that cannot be univocally determined and depends on an agent (e.g. a human individual, a community) acting as black-box.

**Example:** The beauty of that girl.
The style of your clothing.

**Comment:** The word subjective means that a non-well defined or an unknown procedure is used for the definition of the property.

This happens due to e.g. the complexity of the object, the lack of a underlying model for the representation of the object, the non-well specified meaning of the property symbols.

A 'subjective_property' cannot be used to univocally compare 'object'-s.

e.g. you cannot evaluate the beauty of a person on objective basis.

**IRI:** [http://emmc.info/emmo-properties#EMMO_251cfb4f_5c75_4778_91ed_6c8395212fd8](http://emmc.info/emmo-properties#EMMO_251cfb4f_5c75_4778_91ed_6c8395212fd8)

**Relations:**

  - is_a [property](#property)









# Appendix


![The complete EMMO taxonomy.](/home/friisj/Private/prosjekter/EMMC/EMMO-python/examples/emmodoc/output/html_files/entity_graph.pdf)


![EMMO relations.](/home/friisj/Private/prosjekter/EMMC/EMMO-python/examples/emmodoc/output/html_files/relations_graph.pdf)
