import { MATUTINO, VESPERTINO } from "./constants";

export default function Relatorio() {

  const renderMatriculas = (turno, dados) => {
    return (
      <div className="p-6 bg-white rounded-lg shadow-md w-full max-w-lg">
        <h2 className="text-2xl font-semibold mb-6 text-gray-800 border-b-2 border-gray-300 pb-2">{turno}</h2>
        {Object.entries(dados).map(([key, trilha]) => (
          <div key={trilha.id} className="mb-6">
            <h3 className="text-xl font-bold mb-4 text-gray-700">{trilha.nome}</h3>
            <ul className="list-disc list-inside ml-4">
              {trilha.matriculas.map((matricula) => (
                <li key={matricula.cpf} className="mb-2 text-gray-600">
                  <span className="font-medium text-gray-800">{matricula.nome}</span> - CPF: {matricula.cpf}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    );
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
      <div className="bg-r1 h-screen flex flex-col items-center justify-start pt-12 mt-10 px-10 w-full">
        <div className="flex flex-col text-lg text-white font-bold items-center">
          <h1 className="mb-5 text-center text-2xl font-bold mb-12">RELATÓRIO DE MATRÍCULAS</h1>
          <div className="flex space-x-8">
            {renderMatriculas("Turno Matutino", MATUTINO)}
            {renderMatriculas("Turno Vespertino", VESPERTINO)}
          </div>
        </div>
      </div>
    </div>
  );
}
