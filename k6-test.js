import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 50 }, // Acelera para 50 utilizadores simultâneos em 30 seg
    { duration: '1m', target: 50 },  // Mantém os 50 utilizadores durante 1 minuto
    { duration: '10s', target: 0 },  // Desacelera até 0
  ],
};

export default function () {
  // Testa a página principal HTML
  const resHtml = http.get('http://localhost:8000/');
  check(resHtml, {
    'HTML status 200': (r) => r.status === 200,
  });

  // Testa o endpoint da API JSON
  const resApi = http.get('http://localhost:8000/api/produtos/');
  check(resApi, {
    'API status 200': (r) => r.status === 200,
  });

  sleep(1); // Simula o tempo de leitura do utilizador
}