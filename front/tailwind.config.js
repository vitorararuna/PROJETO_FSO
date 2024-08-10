/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        r1: '#20180f',
        r2: '#ff5101',
      },
      width: {
        'webkit-fill-available': '-webkit-fill-available'
      }
    },
  },
  plugins: [],
};