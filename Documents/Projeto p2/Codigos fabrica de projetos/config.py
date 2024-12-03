import os

class Config:
    SECRET_KEY = 'sua_chave_secreta'
    BASE_DIR = os.path.abspath('C:/Users/josep/Documents/projeto cadastro/CÓDIGOS ATUALIZADOS')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/novo_banco.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True 