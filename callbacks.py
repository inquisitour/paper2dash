import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash import dcc, html

def register_callbacks(app):
    @app.callback(
        Output('background-content', 'children'),
        [Input('background-dropdown', 'value')]
    )
    def update_background_content(selected_value):
        if selected_value == 'propositional_language':
            return html.Div([
                html.H2('Propositional Language'),
                html.P("""
                    The language consists of logical connectives (¬, ∨, ∧, ⊃), constants (⊤, ⊥), punctuation symbols, and variables.
                """),
                html.P("""
                    Formulas are constructed inductively, with logical complexity (lc) defined by occurrences of logical symbols.
                """),
                html.P("""
                    Interpretations are sets of variables representing truth assignments.
                """)
            ])
        elif selected_value == 'equilibrium_logic':
            return html.Div([
                html.H2('Equilibrium Logic'),
                html.P("""
                    HT-Logic is based on Kripke semantics with two worlds ("here" (H) and "there" (T)) and a partial ordering H ≤ T.
                """),
                html.P("""
                    HT-Interpretations are ordered pairs \\( \\langle I_H, I_T \\rangle \\) with \\( I_H \\subseteq I_T \\). Truth values are defined for each world, with specific rules for negation, conjunction, disjunction, and implication.
                """),
                html.P("""
                    Models include HT-models and total HT-interpretations \\( \\langle I, I \\rangle \\). A formula is HT-satisfiable if it has an HT-interpretation, and HT-valid if all interpretations satisfy it.
                """),
                html.P("""
                    Equilibrium Models are minimal total HT-interpretations satisfying specific conditions. These models form the basis of nonmonotonic reasoning in equilibrium logic.
                """),
                html.P("""
                    Reasoning Tasks include consistency (existence of equilibrium model), brave reasoning (satisfaction by some equilibrium model), and skeptical reasoning (satisfaction by all equilibrium models).
                """)
            ])
        elif selected_value == 'logic_programs':
            return html.Div([
                html.H2('Logic Programs'),
                html.P("""
                    Logic Programs consist of rules with heads and bodies as expressions (formulas without ⊃).
                """),
                html.P("""
                    Stable Models are derived by minimizing models of program reducts. Program reducts are obtained by evaluating negations with respect to interpretations.
                """),
                html.P("""
                    Examples and Properties illustrate anti-chain properties and equivalences between stable models and equilibrium models.
                """)
            ])
        elif selected_value == 'quantified_propositional_logic':
            return html.Div([
                html.H2('Quantified Propositional Logic'),
                html.P("""
                    The syntax extends classical propositional logic with quantifiers \\( \\forall \\) and \\( \\exists \\). Formulas include bound and free variables, and can be transformed into prenex normal form.
                """),
                html.P("""
                    The semantics are based on evaluations using interpretations. QBFs are evaluated using rules for quantifiers and logical connectives.
                """),
                html.P("""
                    Properties include relations for shifting and renaming quantifiers, and the formation of formulas in prenex normal form.
                """)
            ])

    @app.callback(
        Output('encodings-content', 'children'),
        [Input('encodings-dropdown', 'value')]
    )
    def update_encodings_content(selected_value):
        if selected_value == 'TAU':
            return html.Div([
                html.H2('HT-satisfiability (τ)'),
                dcc.Markdown("""
                    Translation \\( \\tau[\varphi] \\) is inductively defined for atomic formulas, conjunctions, disjunctions, negations, and implications.

                    **Example:** For \\( \\varphi = (p1 ⊃ p2) ⊃ (p3 ⊃ p4) \\), \\( \\tau[\varphi] = ((p1 ⊃ p2) ∧ (p'_1 ⊃ p'_2)) ⊃ ((p3 ⊃ p4) ∧ (p'_3 ⊃ p'_4)) ∧ ((p'_1 ⊃ p'_2) ⊃ (p'_3 ⊃ p'_4)) \\).
                """)
            ])
        elif selected_value == 'THT':
            return html.Div([
                html.H2('Here-and-There Logic (THT)'),
                dcc.Markdown("""
                    Satisfiability in HT is encoded as \\( T_{HT}[\varphi] = (V \leq V') ∧ \\tau[\varphi] \\).

                    The logical complexity of \\( T_{HT}[\varphi] \\) is super-linear in the size of the original formula \\( \\varphi \\).
                """)
            ])
        elif selected_value == 'TE':
            return html.Div([
                html.H2('Equilibrium Logic (TE)'),
                dcc.Markdown("""
                    Equilibrium Model Encoding: \\( T_E[\varphi] = \varphi' ∧ ¬\\exists V ((V < V') ∧ \\tau[\varphi]) \\).

                    The encoding ensures that \\( \\langle I, I \\rangle \\) is an equilibrium model if and only if \\( I' \\) satisfies the formula.
                """)
            ])
        elif selected_value == 'TS':
            return html.Div([
                html.H2('Logic Programs (TS)'),
                dcc.Markdown("""
                    Stable Model Encoding uses \\( \\tau[\cdot] \\) on program rules to form \\( \\tau[\Pi] \\).

                    **Example:** For a program \\( \\Pi = \\{p ← (q ∧ r) ∨ (¬q ∧ ¬s)\\} \\), the reduct and stable model evaluation is demonstrated.

                    Equilibrium Model Encoding for Programs is derived from \\( T_E[\cdot] \\) for logic programs, using transformations that leverage program structure.
                """)
            ])
        elif selected_value == 'CONS':
            return html.Div([
                html.H2('Consistency'),
                dcc.Markdown("""
                    Consistency is encoded by ensuring \\( T \\) has an equilibrium model if \\( \\exists V' T_E[T] \\) is valid.
                """)
            ])
        elif selected_value == 'BRAVE':
            return html.Div([
                html.H2('Brave Reasoning'),
                dcc.Markdown("""
                    Brave Reasoning is encoded by ensuring \\( T \\models_b \varphi \\) if \\( \\exists W' (T_E[T] ∧ \varphi') \\) is valid.
                """)
            ])
        elif selected_value == 'SKEP':
            return html.Div([
                html.H2('Skeptical Reasoning'),
                dcc.Markdown("""
                    Skeptical Reasoning is encoded by ensuring \\( T \\models_s \varphi \\) if \\( \\forall W' (T_E[T] → \varphi') \\) is valid.
                """)
            ])

    @app.callback(
        Output('complexity-content', 'children'),
        [Input('complexity-dropdown', 'value')]
    )
    def update_complexity_content(selected_value):
        if selected_value == 'tasks':
            return html.Div([
                html.H2('Reasoning Tasks'),
                dcc.Markdown("""
                    The primary reasoning tasks in equilibrium logic include:

                    - **Consistency**: Checking whether a given theory has an equilibrium model.
                    - **Brave Reasoning**: Determining if a given formula is satisfied by at least one equilibrium model of a theory.
                    - **Skeptical Reasoning**: Determining if a given formula is satisfied by all equilibrium models of a theory.
                """)
            ])
        elif selected_value == 'proofs':
            return html.Div([
                html.H3("Complexity Proofs"),
                html.P("The paper provides detailed proofs for the complexity results, including:"),
                html.Ul([
                    html.Li("Membership proofs using the quantifier structure of the translations"),
                    html.Li("Hardness proofs by reduction from known hard problems"),
                    html.Li("Proofs for both equilibrium logic and nested logic programs")
                ])
            ])

    @app.callback(
        Output('equivalence-content', 'children'),
        [Input('equivalence-dropdown', 'value')]
    )
    def update_equivalence_content(selected_value):
        if selected_value == 'ordinary':
            return html.Div([
                html.H2('Ordinary Equivalence'),
                dcc.Markdown("""
                    Two theories are ordinarily equivalent if they have the same equilibrium models.

                    Formally, theories T1 and T2 are ordinarily equivalent if for any interpretation I, I is an equilibrium model of T1 if and only if it is an equilibrium model of T2.
                """)
            ])
        elif selected_value == 'strong':
            return html.Div([
                html.H2('Strong Equivalence'),
                dcc.Markdown("""
                    Two theories are strongly equivalent if they remain equivalent when added to any other theory.

                    Formally, theories T1 and T2 are strongly equivalent if for any theory T, the combined theories T1 ∪ T and T2 ∪ T are ordinarily equivalent.
                """)
            ])
        elif selected_value == 'uniform':
            return html.Div([
                html.H2('Uniform Equivalence'),
                dcc.Markdown("""
                    Two theories are uniformly equivalent if they are equivalent under all extensions by a set of facts.

                    Formally, theories T1 and T2 are uniformly equivalent if for any set of facts F, the combined theories T1 ∪ F and T2 ∪ F are ordinarily equivalent.
                """)
            ])

    @app.callback(
        Output('complexity-chart', 'figure'),
        Input('complexity-chart', 'id')
    )
    def update_complexity_chart(_):
        tasks = [
            'HT-satisfiability', 'HT-validity',
            'Consistency (EL/NLP)', 'Brave Reasoning (EL/NLP)', 'Skeptical Reasoning (EL/NLP)',
            'Ordinary Equivalence', 'Uniform Equivalence', 'Strong Equivalence'
        ]
        complexities = ['NP', 'co-NP', 'ΣP2', 'ΣP2', 'ΠP2', 'ΠP2', 'ΠP2', 'co-NP']
        complexity_values = [1, 2, 3, 3, 4, 4, 4, 2]  # Numerical mapping for plot

        df = pd.DataFrame({'Task': tasks, 'Complexity': complexities, 'ComplexityValue': complexity_values})

        fig = go.Figure(data=[go.Bar(x=df['Task'], y=df['ComplexityValue'], text=df['Complexity'], hoverinfo='text')])
        fig.update_layout(
            title='Complexity of Reasoning Tasks and Equivalence Checking',
            xaxis_title='Task',
            yaxis_title='Complexity Class',
            xaxis={'categoryorder': 'total ascending'},
            yaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4],
                ticktext=['NP', 'co-NP', 'ΣP2', 'ΠP2']
            )
        )
        return fig
