#Importando Pacotes 
import pickle
import streamlit as st
import streamlit.components.v1 as components
 
# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva.pkl', 'rb') 
maquina_preditiva = pickle.load(pickle_in)



#Manter a sessão em cache 
@st.cache()
  
# Criando a função que irá fazer a predição usando os dados impostados pelo usuário do Sistema 
def prediction(temp_sensor,temp_silo,temp_amb,aeracao,resfrig,aquec,aquec_direto):  
 
    if aeracao == "Não":
        aeracao = 0
    else:
        aeracao = 1
 
    if resfrig == "Não":
        resfrig = 0
    else:
        resfrig = 1
 
    if aquec == "Não":
        aquec = 0
    else:
        aquec = 1
      
    if aquec_direto == "Não":
        aquec_direto = 0
    else:
        aquec_direto = 1
 

    # Fazendo Predições
    prediction = maquina_preditiva.predict([[temp_sensor,temp_silo,temp_amb,aeracao,resfrig,aquec,aquec_direto]])
    
    if prediction == 'naoeficiente':
        pred = 'não foi eficiente'
    else:
        pred = 'foi eficiente'
    return pred
   
      
  
# Essa função é para criação da webpage  
def main():  
    st.image("silo.png")
    st.title("Aeração")



    
      
    
    
    # embed streamlit docs in a streamlit app
    #components.iframe("https://docs.streamlit.io/en/latest")

      
    # As linhas abaixo criam as caixas na qual o usuário vai entrar com dados da pessoa que quer o empréstimo para fazer a Predição
    temp_sensor = st.number_input('TEMPERATURA DO SENSOR')
    temp_silo = st.number_input('TEMPERATURA DO SILO') 
    temp_amb = st.number_input("TEMPERATURA DO AMB") 
    aeracao = st.selectbox("AERACAO",("Sim","Não"))
    resfrig = st.selectbox('RESFRIAMENTO AERACAO',("Sim","Não"))
    aquec = st.selectbox("AQUECIMENTO AERACAO",("Sim","Não"))
    aquec_direto = st.selectbox("AQUECIMENTO DIRETO AERACÃO",("Sim","Não"))
    result =""




    #Quando o Usuário clicar no botão "Verificar" a Máquina Preditiva faz seu trabalho
    if st.button("Verificar"): 
        result = prediction(temp_sensor,temp_silo,temp_amb,aeracao,resfrig,aquec,aquec_direto) 
        st.success('A aeração  {}'.format(result))
        #print(emprestimo)
     
if __name__=='__main__': 
    main()
