x = 0:0.1:10;
y_sin = sin(x);
y_cos = cos(x);

figure;

subplot(2,1,1);
plot(x, y_sin, 'b');
title('Função Seno');
xlabel('x');
ylabel('sin(x)');
grid on;

subplot(2,1,2);
plot(x, y_cos, 'r');
title('Função Cosseno');
xlabel('x');
ylabel('cos(x)');
grid on;

