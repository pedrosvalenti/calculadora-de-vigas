# Calculadora de Vigas

## Descrição

A **Calculadora de Vigas** é uma aplicação gráfica simples desenvolvida em Python usando Tkinter para auxiliar engenheiros e estudantes no dimensionamento básico de vigas de aço. O programa calcula o momento fletor máximo, o módulo de resistência necessário, a flecha máxima admissível e sugere um perfil de viga I adequado com base nos parâmetros de entrada.

Esta ferramenta é ideal para cálculos rápidos e educacionais em engenharia estrutural, focando em vigas simplesmente apoiadas com carga uniformemente distribuída.

## Funcionalidades

- **Cálculo de Momento Fletor**: Determina o momento máximo para uma viga simplesmente apoiada.
- **Módulo de Resistência**: Calcula o valor necessário de W (cm³) baseado na tensão admissível.
- **Flecha Máxima**: Estima a flecha máxima usando a fórmula L/200.
- **Sugestão de Perfil**: Recomenda perfis I (como I 200, I 300, I 400) com base no W necessário.
- **Interface Gráfica Amigável**: Interface intuitiva com campos de entrada e modal de resultados.
- **Tratamento de Erros**: Validação básica para entradas inválidas.

## Requisitos

- **Python 3.x** (recomendado 3.6 ou superior)
- **Tkinter** (geralmente incluído na instalação padrão do Python)
- **PyInstaller** (opcional, para gerar executável)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/calculadora-de-vigas.git
   cd calculadora-de-vigas
   ```

2. **Instale as dependências** (se necessário):
   - Tkinter geralmente vem com Python. Se não estiver instalado:
     ```bash
     # No Windows
     # Tkinter é incluído por padrão

     # No Linux
     sudo apt-get install python3-tk
     ```

   - Para gerar o executável com PyInstaller:
     ```bash
     pip install pyinstaller
     ```

## Uso

### Executando o Script Python

1. Navegue até a pasta do projeto.
2. Execute o script:
   ```bash
   python script.py
   ```

3. Na interface:
   - Insira o **Comprimento (L)** da viga em metros.
   - Insira a **Carga (q)** uniformemente distribuída em kN/m.
   - Insira a **Tensão (σ)** admissível em kgf/cm².
   - Clique em **CALCULAR**.

4. Um modal aparecerá com os resultados: Momento, W necessário, Flecha máxima e Perfil sugerido.

### Executável (Opcional)

Um executável foi gerado usando PyInstaller e está localizado na pasta `build/script/`. Para usá-lo:

1. Vá para `build/script/`.
2. Execute `script.exe` (no Windows).

Para gerar um novo executável:

```bash
pyinstaller --onefile script.py
```

## Fórmulas Utilizadas

- **Momento Fletor Máximo**: \( M = \frac{q \cdot L^2}{8} \) (kN·m)
- **Módulo de Resistência**: \( W = \frac{M \cdot 100 \cdot 100}{\sigma} \) (cm³) [conversão para unidades consistentes]
- **Flecha Máxima**: \( f_{\max} = \frac{L \cdot 100}{200} \) (cm) [aproximação simplificada]

## Estrutura do Projeto

```
calculadora-de-vigas/
├── script.py          # Código principal da aplicação
├── script.spec        # Arquivo de configuração do PyInstaller
├── build/             # Pasta gerada pelo PyInstaller
│   └── script/
│       ├── script.exe # Executável gerado
│       └── ...        # Outros arquivos de build
└── README.md          # Este arquivo
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs ou sugerir melhorias via [Issues](https://github.com/seu-usuario/calculadora-de-vigas/issues).
- Enviar pull requests com correções ou novas funcionalidades.

Para contribuir:
1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Veja o arquivo LICENSE para mais detalhes.

## Autor

Desenvolvido por [Seu Nome]. Para dúvidas, entre em contato via [email] ou [GitHub Issues].

## Capturas de Tela

*(Adicione capturas de tela da interface aqui)*

- Interface principal
- Modal de resultados

## Agradecimentos

- Inspirado em conceitos básicos de engenharia estrutural.
- Desenvolvido com Python e Tkinter para simplicidade e portabilidade.