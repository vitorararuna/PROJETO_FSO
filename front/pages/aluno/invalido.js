export default function Invalido() {
  return (
    <div class="flex flex-col">
      <div class="flex flex-col bg-r1 flex center p-5">
        <h1>PROJETO FSO 2024.2</h1>
        <hr class="mb-5"></hr>
      </div>
      <div class="bg-r1 h-screen overflow-hidden flex items-center justify-center">
        <div class="bg-white lg:w-5/12 md:w-6/12 w-10/12 shadow-3xl border-4 border-gray-300 rounded-lg">
          <div class="flex items-center justify-center p-12 md:p-24">
            <div class="text-lg text-black font-bold text-center">
              <h1>CPF INVÁLIDO OU SERVIDOR COMPLETAMENTE CHEIO! TENTE NOVAMENTE MAIS TARDE!</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
