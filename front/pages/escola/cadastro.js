import { CPFS } from "@/constants";
import { useState } from "react";

// TODO:
// - maximo de 240 CPFS
// - cpf Invalido
// - conectar com o backend


export default function Cadastro() {
  const [cpf, setCpf] = useState("");
  const [cpfList, setCpfList] = useState([]);

  const formatCpf = (value) => {
    return value
      .replace(/\D/g, "") 
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
  };

  const handleCpfChange = (e) => {
    setCpf(formatCpf(e.target.value));
  };

  const handleCadastro = (e) => {
    e.preventDefault();
    const cpfUnmasked = cpf.replace(/\D/g, "");
    if (cpfUnmasked && !cpfList.includes(cpf)) {
      setCpfList([...cpfList, cpf]);
      setCpf("");
    }
  };

  return (
    <div className="flex flex-col">
      <div className="flex flex-col bg-r1 flex center p-5">
        <h1>PROJETO FSO 2024.2</h1>
        <hr className="mb-5"></hr>
        <h3>Andre Dantas - 211010468</h3>
        <h3>Jean Karia - 211055290</h3>
        <h3>Vitor Araruna - 202060980</h3>
      </div>
      <div className="bg-r1 h-screen flex items-start justify-center pt-12 mt-10 px-10 w-full">
        <div className="flex space-x-8">
          <form
            onSubmit={handleCadastro}
            className="flex flex-col items-center w-full max-w-md bg-white p-6 rounded-lg shadow-md"
            style={{ height: "220px", width: "1200px" }}
          >
            <h2 className="text-2xl font-semibold mb-6 text-gray-800 border-b-2 border-gray-300 pb-2">
              Cadastrar CPF
            </h2>
            <input
              type="text"
              value={cpf}
              onChange={handleCpfChange}
              placeholder="Digite o CPF"
              maxLength={14}
              className="w-full p-3 mb-4 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 text-black"
            />
            <button
              type="submit"
              className="bg-gradient-to-b from-gray-700 to-gray-900 text-white font-medium py-2 px-4 rounded w-full"
            >
              Salvar CPF
            </button>
          </form>
          <div
            className="flex flex-col items-start w-full max-w-md bg-white p-6 rounded-lg shadow-md"
            style={{ maxHeight: "400px", overflowY: "auto" }}
          >
            <h2 className="text-2xl font-semibold mb-6 text-gray-800 border-b-2 border-gray-300 pb-2">
              CPFs Cadastrados
            </h2>
            {cpfList.length === 0 ? (
              <p className="text-gray-600">Nenhum CPF cadastrado ainda.</p>
            ) : (
              <ul className="list-disc list-inside ml-4">
                {cpfList.map((cpf, index) => (
                  <li key={index} className="text-gray-600 mb-2">
                    {cpf}
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
