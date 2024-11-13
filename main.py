import streamlit as st


# Função para calcular a média
def calcular_media(notas):
    if len(notas) > 0:
        return sum(notas) / len(notas)
    else:
        return 0


# Título da aplicação
st.title('Calculadora de Média de Notas')

# Solicitar ao usuário para inserir as notas
st.write('Digite as notas abaixo (separadas por vírgula):')

notas_input = st.text_input('Notas')

# Quando o usuário submeter as notas
if notas_input:
    try:
        # Converter as notas para uma lista de números
        notas = [float(nota.strip()) for nota in notas_input.split(',')]

        # Calcular a média
        media = calcular_media(notas)

        # Exibir o resultado
        st.write(f'A média das notas é: {media:.2f}')

        # Mensagem com base na média
        if media >= 7:
            st.success('Parabéns! Você passou!')
        else:
            st.warning('Você não passou. Tente melhorar na próxima!')
    except ValueError:
        st.error('Por favor, insira apenas números válidos separados por vírgula.')
