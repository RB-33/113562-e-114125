% Definir matriz A e vetor b
A = [3, 2; 1, 4];
b = [10; 12];

% Método 1: Usando a inversa
x1 = inv(A) * b;

% Método 2: Usando A\b
x2 = A \ b;

% Mostrar os resultados
disp('Solução usando inv(A) * b:');
disp(x1);

disp('Solução usando A\\b:');
disp(x2);
