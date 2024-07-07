from dash import dcc, html
import styles

app_layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            html.Div([
                html.H1('Overview'),
                html.Div([
                    html.P("""
                        The paper addresses equilibrium logic, a framework extending stable-model and answer-set semantics to the full propositional language, including nested logic programs.
                    """),
                    html.P("""
                        It provides polynomial reductions of primary reasoning tasks associated with equilibrium logic and nested logic programs into quantified propositional logic (QBF).
                    """),
                    html.P("""
                        The tasks include consistency, brave reasoning, skeptical reasoning, and equivalence testing (ordinary, strong, and uniform equivalence).
                    """),
                    html.P("""
                        The paper offers a uniform axiomatization for a variety of problems using a common language, employing QBF solvers as inference engines, and relating equilibrium logic with circumscription.
                    """)
                ])
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Background', children=[
            html.Div([
                html.H1('Background'),
                dcc.Dropdown(
                    id='background-dropdown',
                    options=[
                        {'label': 'Propositional Language', 'value': 'propositional_language'},
                        {'label': 'Equilibrium Logic', 'value': 'equilibrium_logic'},
                        {'label': 'Logic Programs', 'value': 'logic_programs'},
                        {'label': 'Quantified Propositional Logic', 'value': 'quantified_propositional_logic'}
                    ],
                    value='propositional_language'
                ),
                html.Div(id='background-content')
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Encodings', children=[
            html.Div([
                html.H1('Encodings'),
                dcc.Dropdown(
                    id='encodings-dropdown',
                    options=[
                        {'label': 'HT-satisfiability (τ)', 'value': 'TAU'},
                        {'label': 'Here-and-There Logic (THT)', 'value': 'THT'},
                        {'label': 'Equilibrium Logic (TE)', 'value': 'TE'},
                        {'label': 'Logic Programs (TS)', 'value': 'TS'},
                        {'label': 'Consistency', 'value': 'CONS'},
                        {'label': 'Brave Reasoning', 'value': 'BRAVE'},
                        {'label': 'Skeptical Reasoning', 'value': 'SKEP'}
                    ],
                    value='TAU'
                ),
                html.Div(id='encodings-content')
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Complexity', children=[
            html.Div([
                html.H2("Complexity Results"),
                dcc.Graph(id='complexity-chart'),
                html.Div([
                    html.H3("Complexity Classes"),
                    html.P("NP: Nondeterministic Polynomial Time"),
                    html.P("co-NP: Complement of NP"),
                    html.P("ΣP2: Second level of the polynomial hierarchy (NPNP)"),
                    html.P("ΠP2: Complement of ΣP2")
                ]),
                dcc.Dropdown(
                    id='complexity-dropdown',
                    options=[
                        {'label': 'Reasoning Tasks', 'value': 'tasks'},
                        {'label': 'Complexity Proofs', 'value': 'proofs'}
                    ],
                    value='tasks'
                ),
                html.Div(id='complexity-content')
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Equivalence', children=[
            html.Div([
                html.H1('Equivalence'),
                dcc.Dropdown(
                    id='equivalence-dropdown',
                    options=[
                        {'label': 'Ordinary Equivalence', 'value': 'ordinary'},
                        {'label': 'Strong Equivalence', 'value': 'strong'},
                        {'label': 'Uniform Equivalence', 'value': 'uniform'}
                    ],
                    value='ordinary'
                ),
                html.Div(id='equivalence-content')
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Circumscription', children=[
            html.Div([
                html.H1('Circumscription'),
                dcc.Markdown("""
                    Circumscription is a form of nonmonotonic reasoning introduced by McCarthy in 1980. It aims to infer the minimal models of a theory, making assumptions about the world to minimize the extension of some predicates.

                    In the context of equilibrium logic, circumscription can be related through polynomial reductions. Encodings for equilibrium logic can be shown to correspond to circumscription, extending results for disjunctive logic programs to nested logic programs.
                """),
                html.Div([
                    html.H2('Relation to Circumscription'),
                    dcc.Markdown("""
                        The paper demonstrates the relationship between equilibrium logic and circumscription. It extends Lin's result for disjunctive logic programs to nested logic programs and equilibrium logic.
                    """)
                ])
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Strong Negation', children=[
            html.Div([
                html.H1('Strong Negation'),
                html.P("""
                    Strong negation is an extension of classical negation, allowing for the explicit representation of false information.
                """),
                html.P("""
                    In equilibrium logic, strong negation can be represented and handled within the same framework, providing a more expressive tool for modeling knowledge and reasoning about incomplete or contradictory information.
                """),
                html.P("""
                    The paper discusses the syntactic and semantic integration of strong negation into the logic, as well as its implications for the expressiveness and computational complexity of reasoning tasks.
                """)
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Related Works', children=[
            html.Div([
                html.H1('Related Works'),
                html.P("""
                    The paper situates its contributions within the broader context of nonmonotonic reasoning and logic programming.
                """),
                html.P("""
                    It discusses previous work on stable model semantics, answer set programming, circumscription, and other approaches to nonmonotonic reasoning.
                """),
                html.P("""
                    The related works section highlights how the paper's approach differs from or builds upon these earlier efforts, providing a comprehensive review of the state-of-the-art in the field.
                """)
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Concluding Remarks', children=[
            html.Div([
                html.H1('Concluding Remarks'),
                html.P("""
                    The paper concludes with a summary of the main contributions and findings.
                """),
                html.P("""
                    It highlights the significance of polynomial reductions for reasoning tasks in equilibrium logic and nested logic programs.
                """),
                html.P("""
                    The concluding remarks also suggest directions for future research, including potential extensions of the framework and applications in various domains of artificial intelligence.
                """)
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='Appendix', children=[
            html.Div([
                html.H1('Appendix'),
                html.P("""
                    The appendix provides additional proofs, examples, and technical details that support the main text.
                """),
                html.P("""
                    It includes extended discussions on specific topics, detailed proofs of theorems, and additional examples that illustrate key concepts and results.
                """),
                html.P("""
                    Readers are encouraged to refer to the appendix for a deeper understanding of the technical aspects and for supplementary information that complements the main text.
                """)
            ], style=styles.tab_style)
        ]),
        dcc.Tab(label='References', children=[
            html.Div([
                html.H1('References'),
                dcc.Markdown("""
                        Aguado, F., Cabalar, P., Pérez, G., & Vidal, C. (2008). Strongly equivalent temporal logic programs. In S. Hölldobler, C. Lutz, & H. Wansing (Eds.), Proceedings of the 11th European Conference on Logics in Artificial Intelligence (JELIA 2008) (Vol. 5293, pp. 8-20). Springer.

                        Arieli, O., & Denecker, M. (2003). Reducing preferential paraconsistent reasoning to classical entailment. Journal of Logic and Computation, 13(4), 557-580.

                        Baral, C. (2003). Knowledge Representation, Reasoning and Declarative Problem Solving. Cambridge University Press.

                        Ben-Eliyahu, R., & Dechter, R. (1994). Propositional semantics for disjunctive logic programs. Annals of Mathematics and Artificial Intelligence, 12, 53-87.

                        Besnard, P., Schaub, T., Tompits, H., & Woltran, S. (2005). Representing paraconsistent reasoning via quantified propositional logic. In L. Bertossi, A. Hunter, & T. Schaub (Eds.), Inconsistency Tolerance (Vol. 3300, pp. 84-118). Springer.

                        Biere, A. (2005). Resolve and expand. In H. H. Hoos & D. G. Mitchell (Eds.), Proceedings of the 7th International Conference on Theory and Applications of Satisfiability Testing (SAT 2004) (Vol. 3542, pp. 59-70). Springer.

                        Brewka, G. (2002). Logic programming with ordered disjunction. In Proceedings of the 18th National Conference on Artificial Intelligence (AAAI 2002) (pp. 100-105). AAAI Press.

                        Brewka, G., Niemelä, I., & Syrjänen, T. (2004). Logic programs with ordered disjunctions. Computational Intelligence, 20(2), 335-357.

                        de Bruijn, J., Eiter, T., Polleres, A., & Tompits, H. (2007). Embedding nonground logic programs into autoepistemic logic for knowledge-base combination. In M. Veloso (Ed.), Proceedings of the 20th International Joint Conference on Artificial Intelligence (IJCAI 2007) (pp. 304-309). AAAI Press.

                        Cabalar, P., & Ferraris, P. (2007). Propositional theories are strongly equivalent to logic programs. Theory and Practice of Logic Programming, 7(6), 745-759.

                        Cabalar, P., Pearce, D., & Valverde, A. (2005). Reducing propositional theories in equilibrium logic to logic programs. In C. Bento, A. Cardoso, & G. Dias (Eds.), Proceedings of the 12th Portuguese Conference on Artificial Intelligence (EPIA 2005) (Vol. 3808, pp. 4-17). Springer.

                        Cabalar, P., Pearce, D., & Valverde, A. (2007). Minimal logic programs. In V. Dahl & I. Niemelä (Eds.), Proceedings of the 23rd International Conference on Logic Programming (ICLP 2007) (Vol. 4670, pp. 104-118). Springer.

                        Cabalar, P., & Pérez Vega, G. (2007). Temporal equilibrium logic: A first approach. In R. Moreno-Díaz, F. Pichler, & A. Quesada-Arencibia (Eds.), Proceedings of the 11th International Conference on Computer Aided Systems Theory (EUROCAST 2007) (Vol. 4739, pp. 241-248). Springer.

                        Chen, J. (1993). Minimal knowledge + negation as failure = only knowing (sometimes). In L. M. Pereira & A. Nerode (Eds.), Proceedings of the 2nd International Workshop on Logic Programming and Nonmonotonic Reasoning (LPNMR '93) (pp. 132-150). MIT Press.

                        Chen, Y., Lin, F., & Li, L. (2005). SELP - A system for studying strong equivalence between logic programs. In C. Baral, G. Greco, N. Leone, & G. Terracina (Eds.), Proceedings of the 8th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2005) (Vol. 3662, pp. 442-446). Springer.

                        Church, A. (1956). Introduction to Mathematical Logic, Volume I. Princeton University Press.

                        Clark, K. L. (1978). Negation as failure. In H. Gallaire & J. Minker (Eds.), Logic and Data Bases (pp. 127-138). Plenum Press.

                        van Dalen, D. (1986). Intuitionistic logic. In D. Gabbay & F. Guenthner (Eds.), Handbook of Philosophical Logic, Volume III: Alternatives to Classical Logic (Vol. 166, pp. 225-339). D. Reidel Publishing Co.

                        Delgrande, J., Schaub, T., Tompits, H., & Woltran, S. (2004). On computing solutions to belief change scenarios. Journal of Logic and Computation, 14(6), 801-826.

                        Dix, J., Gottlob, G., & Marek, V. (1996). Reducing disjunctive to non-disjunctive semantics by shift-operations. Fundamenta Informaticae, XXVIII(1/2), 87-100.

                        Egly, U., Eiter, T., Tompits, H., & Woltran, S. (2000). Solving advanced reasoning tasks using quantified Boolean formulas. In Proceedings of the 17th National Conference on Artificial Intelligence (AAAI 2000) (pp. 417-422). AAAI Press/MIT Press.

                        Egly, U., Seidl, M., Tompits, H., Woltran, S., & Zolda, M. (2004). Comparing different prenexing strategies for quantified Boolean formulas. In E. Giunchiglia & A. Tacchella (Eds.), Proceedings of the 6th International Conference on Theory and Applications of Satisfiability Testing (SAT 2003). Selected Revised Papers (Vol. 2919, pp. 214-228). Springer.

                        Egly, U., Seidl, M., & Woltran, S. (2006). A solver for QBFs in nonprenex form. In G. Brewka, S. Coradeschi, A. Perini, & P. Traverso (Eds.), Proceedings of the 17th European Conference on Artificial Intelligence (ECAI 2006) (pp. 477-481). IOS Press.

                        Eiter, T., Faber, W., & Traxler, P. (2005). Testing strong equivalence of nonmonotonic datalog programs - implementation and examples. In C. Baral, G. Greco, N. Leone, & G. Terracina (Eds.), Proceedings of the 8th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2005) (Vol. 3662, pp. 437-441). Springer.

                        Eiter, T., & Fink, M. (2003). Uniform equivalence of logic programs under the stable model semantics. In C. Palamidessi (Ed.), Proceedings of the 19th International Conference on Logic Programming (ICLP 2003) (Vol. 2916, pp. 224-238). Springer.

                        Eiter, T., Fink, M., Tompits, H., & Woltran, S. (2004a). On eliminating disjunctions in stable logic programming. In D. Dubois, C. A. Welty, & M.-A. Williams (Eds.), Proceedings of the 9th International Conference on Principles of Knowledge Representation and Reasoning (KR 2004) (pp. 447-458). AAAI Press.

                        Eiter, T., Fink, M., Tompits, H., & Woltran, S. (2004b). Simplifying logic programs under uniform and strong equivalence. In V. Lifschitz & I. Niemelä (Eds.), Proceedings of the 7th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2004) (Vol. 2923, pp. 87-99). Springer.

                        Eiter, T., Fink, M., & Woltran, S. (2007). Semantical characterizations and complexity of equivalences in answer set programming. ACM Transactions on Computational Logic, 8(3), 1-53.

                        Eiter, T., & Gottlob, G. (1995). On the computational cost of disjunctive logic programming: Propositional case. Annals of Mathematics and Artificial Intelligence, 15(3-4), 289-323.

                        Eiter, T., Gottlob, G., & Mannila, H. (1997). Disjunctive Datalog. ACM Transactions on Database Systems, 22(3), 364-418.

                        Eiter, T., Klotz, V., Tompits, H., & Woltran, S. (2002). Modal nonmonotonic logics revisited: Efficient encodings for the basic reasoning tasks. In U. Egly & C. Fermüller (Eds.), Proceedings of the 11th International Conference on Automated Reasoning with Analytic Tableaux and Related Methods (TABLEAUX 2002) (Vol. 2381, pp. 100-114). Springer.

                        Eiter, T., Tompits, H., & Woltran, S. (2005). On solution correspondences in answer set programming. In L. Pack Kaelbling & A. Saffiotti (Eds.), Proceedings of the 19th International Joint Conference on Artificial Intelligence (IJCAI 2005) (pp. 97-102). Professional Book Center.

                        Erdem, E., & Lifschitz, V. (2001). Fages’ theorem for programs with nested expressions. In P. Codognet (Ed.), Proceedings of the 18th International Conference on Logic Programming (ICLP 2001) (Vol. 2237, pp. 242-254). Springer.

                        Erdem, E., & Lifschitz, V. (2003). Tight logic programs. Theory and Practice of Logic Programming, 3(4-5), 499-518.

                        Faber, W., & Konczak, K. (2005). Strong equivalence for logic programs with preferences. In L. Pack Kaelbling & A. Saffiotti (Eds.), Proceedings of the 19th International Joint Conference on Artificial Intelligence (IJCAI 2005) (pp. 430-435). Professional Book Center.

                        Faber, W., Tompits, H., & Woltran, S. (2008). Notions of strong equivalence for logic programs with ordered disjunction. In G. Brewka & J. Lang (Eds.), Proceedings of the 11th International Conference on Principles of Knowledge Representation and Reasoning (KR 2008) (pp. 433-443). AAAI Press.

                        Fages, F. (1994). Consistency of Clark’s completion and existence of stable models. Methods of Logic in Computer Science, 1, 51-60.

                        Ferraris, P. (2005). Answer sets for propositional theories. In C. Baral, G. Greco, N. Leone, & G. Terracina (Eds.), Proceedings of the 8th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2005) (Vol. 3662, pp. 119-131). Springer.

                        Ferraris, P., Lee, J., & Lifschitz, V. (2006). A generalization of the Lin-Zhao theorem. Annals of Mathematics and Artificial Intelligence, 47(1-2), 79-101.

                        Ferraris, P., Lee, J., & Lifschitz, V. (2007). A new perspective on stable models. In M. Veloso (Ed.), Proceedings of the 20th International Joint Conference on Artificial Intelligence (IJCAI 2007) (pp. 372-379). AAAI Press.

                        Fink, M. (2008). Equivalences in answer-set programming by countermodels in the logic of here-and-there. In M. G. de la Banda & E. Pontelli (Eds.), Proceedings of the 24th International Conference on Logic Programming (ICLP 2008) (Vol. 5366, pp. 99-113). Springer.

                        Garey, M. R., & Johnson, D. S. (1979). Computers and Intractability. W. H. Freeman.

                        Gebser, M., Lee, J., & Lierler, Y. (2006). Elementary sets for logic programs. In Proceedings of the 21st National Conference on Artificial Intelligence (AAAI 2006) (pp. 244-249). AAAI Press.

                        Gebser, M., Schaub, T., Tompits, H., & Woltran, S. (2008). Alternative characterizations for program equivalence under answer-set semantics based on unfounded sets. In S. Hartmann & G. Kern-Isberner (Eds.), Proceedings of the 5th International Symposium on Foundations of Information and Knowledge Systems (FoIKS 2008) (Vol. 4932, pp. 24-41). Springer.

                        van Gelder, A., Ross, K., & Schlipf, J. (1991). The well-founded semantics for general logic programs. Journal of the ACM, 38(3), 620-650.

                        Gelfond, M. (1987). On stratified autoepistemic theories. In K. Forbus & H. E. Shrobe (Eds.), Proceedings of the 6th National Conference on Artificial Intelligence (AAAI '87) (pp. 207-211). AAAI Press/MIT Press.

                        Gelfond, M., & Lifschitz, V. (1991). Classical negation in logic programs and disjunctive databases. New Generation Computing, 9(3-4), 365-385.

                        Gelfond, M., Lifschitz, V., Przymusinska, H., & Schwarz, G. (1994). Autoepistemic logic and introspective circumscription. In R. Fagin (Ed.), Proceedings of the 5th Conference on Theoretical Aspects of Reasoning about Knowledge (TARK '94) (pp. 197-207).

                        Gelfond, M., Lifschitz, V., Przymusinska, H., & Truszczyński, M. (1991). Disjunctive defaults. In J. Allen, R. Fikes, & B. Sandewall (Eds.), Proceedings of the 2nd Conference on Principles of Knowledge Representation and Reasoning (KR '91) (pp. 230-237). Morgan Kaufmann.

                        Gelfond, M., Przymusinska, H., & Przymusinski, T. C. (1989). On the relationship between circumscription and negation as failure. Artificial Intelligence, 38(1), 75-94.

                        Gelfond, M., Przymusinska, H., & Przymusinski, T. C. (1990). On the relationship between CWA, minimal model, and minimal Herbrand model semantics. International Journal of Intelligent Systems, 5, 549-564.

                        Giunchiglia, E., Narizzano, M., & Tacchella, A. (2003). Backjumping for quantified Boolean logic satisfiability. Artificial Intelligence, 145, 99-120.

                        Gödel, K. (1932). Zum intuitionistischen Aussagenkalkül. Anzeiger der Akademie der Wissenschaften in Wien, 65-66.

                        Gurevich, Y. (1977). Intuitionistic logic with strong negation. Studia Logica, 36(1-2), 49-59.

                        Heyting, A. (1930). Die formalen Regeln der intuitionistischen Logik. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 42-56. Reprint in Logik-Texte: Kommentierte Auswahl zur Geschichte der Modernen Logik, Akademie-Verlag, 1986.

                        Inoue, K., & Sakama, C. (1998). Negation as failure in the head. Journal of Logic Programming, 35(1), 39-78.

                        Inoue, K., & Sakama, C. (2004). Equivalence of logic programs under updates. In J. J. Alferes & J. A. Leite (Eds.), Proceedings of the 9th European Conference on Logics in Artificial Intelligence (JELIA 2004) (Vol. 3229, pp. 174-186). Springer.

                        Janhunen, T. (2001). On the effect of default negation on the expressiveness of disjunctive rules. In T. Eiter, W. Faber, & M. Truszczyński (Eds.), Proceedings of the 6th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2001) (Vol. 2173, pp. 93-106). Springer.

                        Janhunen, T. (2004). Representing normal programs with clauses. In R. L. de Mántaras & L. Saitta (Eds.), Proceedings of the 16th European Conference on Artificial Intelligence (ECAI 2004) (pp. 358-362). IOS Press.

                        Janhunen, T., & Oikarinen, E. (2002). Testing the equivalence of logic programs under stable model semantics. In S. Flesca, S. Greco, N. Leone, & G. Ianni (Eds.), Proceedings of the 8th European Conference on Logics in Artificial Intelligence (JELIA 2002) (Vol. 2424, pp. 493-504). Springer.

                        de Jongh, D., & Hendriks, L. (2003). Characterizations of strongly equivalent logic programs in intermediate logics. Theory and Practice of Logic Programming, 3(3), 259-270.

                        Kowalski, V. (1968). The calculus of the weak “law of excluded middle”. Mathematics of the USSR, 8, 648-658.

                        Lee, J. (2005). A model-theoretic counterpart of loop formulas. In L. Pack Kaelbling & A. Saffiotti (Eds.), Proceedings of the 19th International Joint Conference on Artificial Intelligence (IJCAI 2005) (pp. 503-508). Professional Book Center.

                        Lee, J., & Lifschitz, V. (2003). Loop formulas for disjunctive logic programs. In C. Palamidessi (Ed.), Proceedings of the 19th International Conference on Logic Programming (ICLP 2003) (Vol. 2916, pp. 451-465). Springer.

                        Lee, J., Lifschitz, V., & Palla, R. (2008). A reductive semantics for counting and choice in answer set programming. In D. Fox & C. P. Gomes (Eds.), Proceedings of the 23rd National Conference on Artificial Intelligence (AAAI 2008) (pp. 472-479). AAAI Press.

                        Leone, N., Pfeifer, G., Faber, W., Eiter, T., Gottlob, G., Perri, S., & Scarcello, F. (2006). The DLV system for knowledge representation and reasoning. ACM Transactions on Computational Logic, 7(3), 499-562.

                        Leśniewski, S. (1929). Grundzüge eines neuen Systems der Grundlagen der Mathematik. Fundamenta Mathematica, 14, 1-81.

                        Letz, R. (2002). Lemma and model caching in decision procedures for quantified Boolean formulas. In U. Egly & C. Fermüller (Eds.), Proceedings of the 11th International Conference on Automated Reasoning with Analytic Tableaux and Related Methods (TABLEAUX 2002) (Vol. 2381, pp. 160-175). Springer.

                        Lierler, Y. (2005). Disjunctive answer set programming via satisfiability. In C. Baral, G. Greco, N. Leone, & G. Terracina (Eds.), Proceedings of the 8th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2005) (Vol. 3662, pp. 447-451). Springer.

                        Lifschitz, V. (1989). Between circumscription and autoepistemic logic. In R. Brachman, H. Levesque, & R. Reiter (Eds.), Proceedings of the 1st International Conference on Principles of Knowledge Representation and Reasoning (KR '89) (pp. 235-244). Morgan Kaufmann.

                        Lifschitz, V. (1994). Circumscription. In D. M. Gabbay, C. J. Hogger, & J. A. Robinson (Eds.), Handbook of Logic in Artificial Intelligence and Logic Programming (pp. 297-352). Clarendon Press.

                        Lifschitz, V., Pearce, D., & Valverde, A. (2001). Strongly equivalent logic programs. ACM Transactions on Computational Logic, 2(4), 526-541.

                        Lifschitz, V., Pearce, D., & Valverde, A. (2007). A characterization of strong equivalence for logic programs with variables. In C. Baral, G. Brewka, & J. S. Schlipf (Eds.), Proceedings of the 9th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2007) (Vol. 4483, pp. 188-200). Springer.

                        Lifschitz, V., & Schwarz, G. (1993). Extended logic programs as autoepistemic theories. In L. M. Pereira & A. Nerode (Eds.), Proceedings of the 2nd International Workshop on Logic Programming and Nonmonotonic Reasoning (LPNMR '93) (pp. 101-114). MIT Press.

                        Lifschitz, V., Tang, L., & Turner, H. (1999). Nested expressions in logic programs. Annals of Mathematics and Artificial Intelligence, 25(3-4), 369-389.

                        Lifschitz, V., & Turner, H. (1994). Splitting a logic program. In Proceedings of the 11th International Conference on Logic Programming (ICLP '94) (pp. 23-38). MIT Press.

                        Lin, F. (1991). A Study of Nonmonotonic Reasoning. Ph.D. thesis, Stanford University, California, USA.

                        Lin, F. (2002). Reducing strong equivalence of logic programs to entailment in classical propositional logic. In D. Fensel, F. Giunchiglia, D. McGuinness, & M.-A. Williams (Eds.), Proceedings of the 8th International Conference on Principles of Knowledge Representation and Reasoning (KR 2002) (pp. 170-176). Morgan Kaufmann.

                        Lin, F., & Zhao, Y. (2002). ASSAT: Computing answer sets of a logic program by SAT solvers. In Proceedings of the 18th National Conference on Artificial Intelligence (AAAI 2002) (pp. 112-117). AAAI Press/MIT Press.

                        Linke, T., Tompits, H., & Woltran, S. (2004). On acyclic and head-cycle free nested logic programs. In B. Demoen & V. Lifschitz (Eds.), Proceedings of the 20th International Conference on Logic Programming (ICLP 2004) (Vol. 3132, pp. 225-239). Springer.

                        Liu, L., & Truszczyński, M. (2005). Properties of programs with monotone and convex constraints. In M. Veloso & S. Kambhampati (Eds.), Proceedings of the 20th National Conference on Artificial Intelligence (AAAI 2005) (pp. 701-706). AAAI Press.

                        Lukasiewicz, J., & Tarski, A. (1930). Untersuchungen über den Aussagenkalkül. Comptes Rendus Séances Société des Sciences et Lettres Varsovie, 23, 30-50.

                        Maher, M. J. (1988). Equivalence of logic programs. In J. Minker (Ed.), Foundations of Deductive Databases and Logic Programming (pp. 627-658). Morgan Kaufmann.

                        Marek, V. W., & Truszczyński, M. (1993). Reflexive autoepistemic logic and logic programming. In L. M. Pereira & A. Nerode (Eds.), Proceedings of the 2nd International Workshop on Logic Programming and Nonmonotonic Reasoning (LPNMR '93) (pp. 115-131). MIT Press.

                        McCarthy, J. (1980). Circumscription - a form of nonmonotonic reasoning. Artificial Intelligence, 13, 27-39.

                        McCluskey, E. J. (1956). Minimization of boolean functions. Bell System Technical Journal, 35, 1417-1444.

                        Meyer, A. R., & Stockmeyer, L. J. (1973). Word problems requiring exponential time. In ACM Symposium on Theory of Computing (STOC '73) (pp. 1-9). ACM Press.

                        Moore, R. C. (1985). Semantical considerations on nonmonotonic logic. Artificial Intelligence, 25, 75-94.

                        Mundici, D. (1987). Satisfiability in many-valued sentential logic is NP-complete. Theoretical Computer Science, 52(1-2), 145-153.

                        Nelson, D. (1949). Constructible falsity. Journal of Symbolic Logic, 14(2), 16-26.

                        Oetsch, J., Seidl, M., Tompits, H., & Woltran, S. (2006a). cc⊤: A correspondence-checking tool for logic programs under the answer-set semantics. In M. Fisher, W. van der Hoek, B. Konev, & A. Lisitsa (Eds.), Proceedings of the 10th European Conference on Logics in Artificial Intelligence (JELIA 2006) (Vol. 4160, pp. 502-505). Springer.

                        Oetsch, J., Seidl, M., Tompits, H., & Woltran, S. (2006b). cc⊤: A tool for checking advanced correspondence problems in answer-set programming. In A. Gelbukh & S. S. Guerra (Eds.), Proceedings of the 15th International Conference on Computing (CIC 2006) (pp. 3-10). IEEE Computer Society Press.

                        Oetsch, J., Seidl, M., Tompits, H., & Woltran, S. (2007). An extension of the system cc⊤ for testing relativised uniform equivalence under answer-set projection. In Proceedings of the 16th International Conference on Computing (CIC 2007).

                        Oetsch, J., Tompits, H., & Woltran, S. (2007). Facts do not cease to exist because they are ignored: Relativised uniform equivalence with answer-set projection. In Proceedings of the 22nd National Conference on Artificial Intelligence (AAAI 2007) (pp. 458-464). AAAI Press.

                        Oikarinen, E., & Janhunen, T. (2004). Verifying the equivalence of logic programs in the disjunctive case. In V. Lifschitz & I. Niemelä (Eds.), Proceedings of the 7th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2004) (Vol. 2923, pp. 180-193). Springer.

                        Oikarinen, E., & Janhunen, T. (2006). Modular equivalence for normal logic programs. In J. Dix & A. Hunter (Eds.), Proceedings of the 11th International Workshop on Nonmonotonic Reasoning (NMR 2006) (pp. 10-18). University of Clausthal, Department of Informatics, Technical Report, IfI-06-04.

                        Osorio, M., Navarro, J. A., & Arrazola, J. (2005). Safe beliefs for propositional theories. Annals of Pure and Applied Logic, 134(1), 63-82.

                        Papadimitriou, C. (1994). Computational Complexity. Addison-Wesley.

                        Pearce, D. (1997). A new logical characterisation of stable models and answer sets. In J. Dix, L. Pereira, & T. Przymusinski (Eds.), Non-Monotonic Extensions of Logic Programming (Vol. 1216, pp. 57-70). Springer.

                        Pearce, D. (1999). From here to there: Stable negation in logic programming. In D. Gabbay & H. Wansing (Eds.), What is Negation? (pp. 161-181). Kluwer.

                        Pearce, D. (2004). Simplifying logic programs under answer set semantics. In B. Demoen & V. Lifschitz (Eds.), Proceedings of the 20th International Conference on Logic Programming (ICLP 2004) (Vol. 3132, pp. 210-224). Springer.

                        Pearce, D. (2006). Equilibrium logic. Annals of Mathematics and Artificial Intelligence, 47, 3-41.

                        Pearce, D., de Guzmán, I., & Valverde, A. (2000a). Computing equilibrium models using signed formulas. In J. Lloyd, V. Dahl, U. Furbach, M. Kerber, K.-K. Lau, C. Palamidessi, L. M. Pereira, Y. Sagiv, & P. J. Stuckey (Eds.), Proceedings of the 1st International Conference on Computational Logic (CL 2000) (Vol. 1861, pp. 688-702). Springer.

                        Pearce, D., de Guzmán, I., & Valverde, A. (2000b). A tableau calculus for equilibrium entailment. In R. Dyckhoff (Ed.), Proceedings of the 9th International Conference on Automated Reasoning with Analytic Tableaux and Related Methods (TABLEAUX 2000) (Vol. 1847, pp. 352-367). Springer.

                        Pearce, D., Sarsakov, V., Schaub, T., Tompits, H., & Woltran, S. (2002). A polynomial translation of logic programs with nested expressions into disjunctive logic programs: Preliminary report. In P. Stuckey (Ed.), Proceedings of the 19th International Conference on Logic Programming (ICLP 2002) (Vol. 2401, pp. 405-420). Springer.

                        Pearce, D., Tompits, H., & Woltran, S. (2001). Encodings for equilibrium logic and logic programs with nested expressions. In P. Brazdil & A. Jorge (Eds.), Proceedings of the 10th Portuguese Conference on Artificial Intelligence (EPIA 2001) (Vol. 2258, pp. 306-320). Springer.

                        Pearce, D., & Valverde, A. (2004a). Synonymous theories in answer set programming and equilibrium logic. In Proceedings 16th European Conference on Artificial Intelligence (ECAI 2004) (pp. 388-392).

                        Pearce, D., & Valverde, A. (2004b). Uniform equivalence for equilibrium logic and logic programs. In V. Lifschitz & I. Niemelä (Eds.), Proceedings of the 7th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2004) (Vol. 2923, pp. 194-206). Springer.

                        Pearce, D., & Valverde, A. (2005). A first order nonmonotonic extension of constructive logic. Studia Logica, 80(2-3), 321-346.

                        Pearce, D., & Valverde, A. (2008). Quantified equilibrium logic and foundations for answer set programs. In M. G. de la Banda & E. Pontelli (Eds.), Proceedings of the 24th International Conference on Logic Programming (ICLP 2008) (Vol. 5366, pp. 546-560). Springer.

                        Pearce, D., & Wagner, G. (1991). Logic programming with strong negation. In P. Schroeder-Heiste (Ed.), Workshop on Extensions of Logic Programming, Proceedings (Vol. 475, pp. 311-326). Springer.

                        Perlis, D. (1988). Autocircumscription. Artificial Intelligence, 36, 223-236.

                        Przymusinski, T. C. (1991). Stable semantics for disjunctive programs. New Generation Computing, 9(3-4), 401-424.

                        Pührer, J., Tompits, H., & Woltran, S. (2008). Elimination of disjunction and negation in answer-set programs under hyperequivalence. In M. G. de la Banda & E. Pontelli (Eds.), Proceedings of the 24th International Conference on Logic Programming (ICLP 2008) (Vol. 5366, pp. 561-575). Springer.

                        Quine, W. V. O. (1952). The problem of simplifying truth functions. American Mathematical Monthly, 59, 521-531.

                        Rintanen, J. (1999). Constructing conditional plans by a theorem prover. Journal of Artificial Intelligence Research, 10, 323-352.

                        Russell, B. (1906). The theory of implication. American Journal of Mathematics, 28(2), 159-202.

                        Sagiv, Y. (1988). Optimising datalog programs. In J. Minker (Ed.), Foundations of Deductive Databases and Logic Programming (pp. 659-698). Morgan Kaufmann.

                        Sarsakov, V., Schaub, T., Tompits, H., & Woltran, S. (2004). nlp: A compiler for nested logic programming. In V. Lifschitz & I. Niemelä (Eds.), Proceedings of the 7th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2004) (Vol. 2923, pp. 361-364). Springer.

                        Simons, P., Niemelä, I., & Soininen, T. (2002). Extending and implementing the stable model semantics. Artificial Intelligence, 138, 181-234.

                        Srzednicki, J., & Stachniak, Z. (Eds.). (1998). Lesniewski’s Systems Protothetic. Dordrecht.

                        Stockmeyer, L. J. (1976). The polynomial-time hierarchy. Theoretical Computer Science, 3(1), 1-22.

                        Tompits, H. (2003). Expressing default abduction problems as quantified Boolean formulas. AI Communications, 16(2), 89-105.

                        Tompits, H., & Woltran, S. (2005). Towards implementations for advanced equivalence checking in answer-set programming. In M. Gabbrielli & G. Gupta (Eds.), Proceedings of the 21st International Conference on Logic Programming (ICLP 2005) (Vol. 3668, pp. 189-203). Springer.

                        Truszczyński, M., & Woltran, S. (2008). Hyperequivalence of logic programs with respect to supported models. In D. Fox & C. P. Gomes (Eds.), Proceedings of the 23rd National Conference on Artificial Intelligence (AAAI 2008) (pp. 560-565). AAAI Press.

                        Turner, H. (2001). Strong equivalence for logic programs and default theories (made easy). In T. Eiter, W. Faber, & M. Truszczyński (Eds.), Proceedings of the 6th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2001) (Vol. 2173, pp. 81-92). Springer.

                        Turner, H. (2003). Strong equivalence made easy: Nested expressions and weight constraints. Theory and Practice of Logic Programming, 3(4-5), 609-622.

                        Valverde, A. (2004). tabeql: A tableau based suite for equilibrium logic. In J. J. Alferes & J. A. Leite (Eds.), Proceedings of the 9th European Conference on Logics in Artificial Intelligence (JELIA 2004) (Vol. 3229, pp. 734-737). Springer.

                        Vorob’ev, N. (1952). A constructive propositional calculus with strong negation (in Russian). Doklady Akademii Nauk SSR, 85, 689-692.

                        Whitehead, A. N., & Russell, B. (1910–1913). Principia Mathematica. Vol. 1-3. Cambridge University Press.

                        Woltran, S. (2003). Quantified Boolean Formulas - From Theory to Practice. Ph.D. thesis, Technische Universität Wien, Institut für Informationssysteme.

                        Woltran, S. (2004). Characterizations for relativized notions of equivalence in answer set programming. In J. J. Alferes & J. A. Leite (Eds.), Proceedings of the 9th European Conference on Logics in Artificial Intelligence (JELIA 2004) (Vol. 3229, pp. 161-173). Springer.

                        Woltran, S. (2005). Answer set programming: Model applications and proofs-of-concept. Tech. Rep. WP5, Working Group on Answer Set Programming (WASP, IST-FET-2001-37004). Available at http://www.kr.tuwien.ac.at/research/projects/WASP/.

                        Woltran, S. (2008). A common view on strong, uniform, and other notions of equivalence in answer-set programming. Theory and Practice of Logic Programming, 8(2), 217-234.

                        Wrathall, C. (1976). Complete sets and the polynomial-time hierarchy. Theoretical Computer Science, 3(1), 23-33.

                        You, J.-H., Yuan, L.-Y., & Mingyi, Z. (2003). On the equivalence between answer sets and models of completion for nested logic programs. In G. Gottlob & T. Walsh (Eds.), Proceedings of the 18th International Joint Conference on Artificial Intelligence (IJCAI 2003) (pp. 859-865). Morgan Kaufmann.

                        Yuan, L.-Y. (1994). Autoepistemic logic of first order and its expressive power. Journal of Automated Reasoning, 13(1), 69-82.
                """)
            ], style=styles.tab_style)
        ])
    ])
], style=styles.main_style)
