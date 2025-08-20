from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sicredi - Atualização de Cadastro</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            .header { text-align: center; margin-bottom: 30px; }
            .logo { color: #00a651; font-size: 24px; font-weight: bold; }
            .title { color: #333; margin: 20px 0; }
            .form-group { margin-bottom: 20px; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input, select { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
            .btn { background: #00a651; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
            .btn:hover { background: #008a43; }
            .footer { text-align: center; margin-top: 30px; color: #666; font-size: 12px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">SICREDI</div>
                <h1 class="title">Atualização de Cadastro</h1>
                <p>Mantenha seus dados sempre atualizados</p>
            </div>
            
            <form>
                <div class="form-group">
                    <label>Tipo de Pessoa:</label>
                    <select>
                        <option>Pessoa Física</option>
                        <option>Pessoa Jurídica</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Nome Completo:</label>
                    <input type="text" placeholder="Digite seu nome completo">
                </div>
                
                <div class="form-group">
                    <label>CPF/CNPJ:</label>
                    <input type="text" placeholder="Digite seu CPF ou CNPJ">
                </div>
                
                <div class="form-group">
                    <label>Email:</label>
                    <input type="email" placeholder="Digite seu email">
                </div>
                
                <div class="form-group">
                    <label>Telefone:</label>
                    <input type="tel" placeholder="Digite seu telefone">
                </div>
                
                <div class="form-group">
                    <label>
                        <input type="checkbox" style="width: auto; margin-right: 10px;">
                        Aceito os termos de uso e política de privacidade
                    </label>
                </div>
                
                <button type="submit" class="btn">Atualizar Cadastro</button>
            </form>
            
            <div class="footer">
                <p>© 2025 Sicredi - Todos os direitos reservados</p>
                <p>Esta aplicação está em conformidade com a LGPD</p>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
