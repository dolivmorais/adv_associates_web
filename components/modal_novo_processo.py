from logging import exception
import dash
import plotly.express as px
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc
from datetime import timedelta, date

import json
import pandas as pd

from app import app
from sql_beta import df_proc, df_adv

col_centered_style={'display': 'flex', 'justify-content': 'center'}

# ========= Layout ========= #
layout = dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Adicione Um Processo")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        # Empresa
                        dbc.Label('Empresa', html_for='empresa_matriz'),
                        dcc.Dropdown(id='empresa_matriz', clearable=False, className='dbc',
                            options=['Escritório Matriz', 'Filial Porto Alegre', 'Filial Curitiba', 'Filial Canoas']),
                        # Tipo de Processo
                        dbc.Label('Tipo de Processo', html_for='tipo_processo'),
                        dcc.Dropdown(id='tipo_processo', clearable=False, className='dbc',
                            options=['Civil', 'Criminal', 'Previdenciário', 'Trabalhista', 'Vara de Família']),
                        # Tipo de Processo
                        dbc.Label('Ação', html_for='acao'),
                        dcc.Dropdown(id='acao', clearable=False, className='dbc',
                            options=['Alimentos', 'Busca e Apreensão', 'Cautelar Inominada', 'Consignação', 'Habeas Corpus', 'Mandado de Segurança', 'Reclamação']),
                    ], sm=12, md=4),
                    dbc.Col([
                        dbc.Label("Descrição", html_for='input_desc'),
                        dbc.Textarea(id="input_desc", placeholder="Escreva aqui observações sobre o processo...", style={'height': '80%'}),
                    ], sm=12, md=8)
                ]),
                html.Hr(),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Vara", html_for='vara'),
                        dbc.RadioItems(id='vara',
                            options=[{'label': 'Civil', 'value': 'Civil'},
                            {'label': 'Conciliação e Julgamento', 'value': 'Conciliação e Julgamento'},
                            {'label': 'Trabalhista', 'value': 'Trabalhista'},
                            {'label': 'Vara de Família', 'value': 'Vara de Família'}])
                    ], sm=12, md=4),
                    dbc.Col([
                        dbc.Label("Fase", html_for='fase'),
                        dbc.RadioItems(id='fase', inline=True,
                            options=[{'label': 'Elaboração', 'value': 'Elaboração'},
                            {'label': 'Execução', 'value': 'Execução'},
                            {'label': 'Impugnação', 'value': 'Impugnação'},
                            {'label': 'Instrução', 'value': 'Instrução'},
                            {'label': 'Recurso', 'value': 'Recurso'},
                            {'label': 'Suspenso', 'value': 'Suspenso'}])
                    ], sm=12, md=5),
                    dbc.Col([
                        dbc.Label("Instância", html_for='instancia'),
                        dbc.RadioItems(id='instancia',
                            options=[{'label': '1A Instância', 'value': 1},
                            {'label': '2A Instância', 'value': 2},])
                    ], sm=12, md=3)
                ]),
            ])

    ], id='modal_processo', size='lg', is_open=True)



# ======= Callbacks ======== #
# Callback para abrir o modal


# Callback para CRUD de processos


# Callback pra atualizar o dropdown de advogados
