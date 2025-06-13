% Script para avaliar y(x) = x^2 - 3x + 2 entre -1 e 3 com passo 0.01

% Intervalo de x
x = -1:0.01:3;

% -----------------------
% Método 1: Usando ciclo for
% -----------------------
y_for = zeros(size(x)); % Pré-alocar vetor
tic
for i = 1:length(x)
    y_for(i) = x(i)^2 - 3*x(i) + 2;
end
tempo_for = toc;
fprintf('Tempo com ciclo for: %.6f segundos\n', tempo_for);

% -----------------------
% Método 2: Usando vetorização
% -----------------------
tic
y_vect = x.^2 - 3*x + 2;
tempo_vect = toc;
fprintf('Tempo com vetorização: %.6f segundos\n', tempo_vect);

% -----------------------
% Gráfico
% -----------------------
figure
plot(x, y_vect, 'b', 'LineWidth', 2)
title('Gráfico do Polinómio y(x) = x^2 - 3x + 2')
xlabel('x')
ylabel('y(x)')
grid on
legend('y(x)')
