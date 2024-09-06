import api from "./config";


export const request_login = async (cpf) => {
    try {
        const response = await api
            .get("/aluno/login", {
                params: { cpf: cpf },
            });
        return response.data;
    } catch (error) {
        console.error("Erro ao realizar login:", error);
        throw error;
    }
  };


  export const request_turnos = async () => {
    try {
        const response = await api
            .get("/turnos");
        return response.data;
    } catch (error) {
        console.error("Erro ao resgatar turnos", error);
        throw error;
    }
  };

  export const request_matutino = async () => {
    try {
        const response = await api
            .get("/matutino/turmas");
        return response.data;
    } catch (error) {
        console.error("Erro ao resgatar turmas matutino", error);
        throw error;
    }
  };

  export const request_vespertino = async () => {
    try {
        const response = await api
            .get("/vespertino/turmas");
        return response.data;
    } catch (error) {
        console.error("Erro ao resgatar turmas vespertino", error);
        throw error;
    }
  };

  export const request_realizar_matricula = async (cpf, turma_id) => {
    try {
      const requestBody = {
        cpf,
        turma_id,
      };

      console.log('Enviando dados para matrícula:', requestBody);

  
      const response = await api.post("/aluno/realizar_matricula", requestBody);
      return response.data;
    } catch (error) {
      console.error("Erro ao realizar matrícula", error);
      throw error;
    }
  };