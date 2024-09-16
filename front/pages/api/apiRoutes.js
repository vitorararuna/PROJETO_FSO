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


  export const request_aluno_reservas_disponíveis = async (cpf) => {
    try {
        const response = await api
            .get("aluno/reservas", {
              params: { cpf: cpf },
          });
        return response.data;
    } catch (error) {
        console.error("Erro ao resgatar reservas disponíveis", error);
        throw error;
    }
  };

  export const request_cadastrados = async () => {
    try {
        const response = await api
            .get("adm/cadastrados");
        return response.data;
    } catch (error) {
        console.error("Erro ao resgatar cadastrados disponíveis", error);
        throw error;
    }
  };

  export const request_cadastrar_cpf = async (cpf, name) => {
    try {
      const requestBody = {
        cpf,
        name,
      };
  
      const response = await api.post("/escola/cadastrar_cpf", requestBody);
      return response.data;
    } catch (error) {
      console.error("Erro ao cadastrar cpf", error);
    }
  };

  export const request_adm_relatorio = async () => {
    try {
        const response = await api
            .get("adm/relatorio");
        return response.data;
    } catch (error) {
        console.error("Erro ao resgatar relatório", error);
        throw error;
    }
  };


  export const request_logout = async (cpf) => {
    try {
        const response = await api
            .get("/aluno/timeOut", {
                params: { cpf: cpf },
            });
        return response.data;
    } catch (error) {
        console.error("Erro ao realizar logout:", error);
        throw error;
    }
  };