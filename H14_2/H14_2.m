% Modified lqsfit.m to read from input1.dat

% Purpose:
% To perform a least-squares fit of an input data set
% to a straight line, and print out the resulting slope
% and intercept values. The input data comes from a file.

% Read the input data from the ASCII file
data = load('input1.dat');  % Load all the data into a matrix
x = data(:,1);               % First column is x
y = data(:,2);               % Second column is y

% Determine number of points
n_points = length(x);

% Accumulate statistics
sum_x = sum(x);
sum_y = sum(y);
sum_x2 = sum(x.^2);
sum_xy = sum(x .* y);

x_bar = sum_x / n_points;
y_bar = sum_y / n_points;

% Calculate slope and intercept
slope = (sum_xy - sum_x * y_bar) / (sum_x2 - sum_x * x_bar);
y_int = y_bar - slope * x_bar;

% Tell user
disp('Regression coefficients for the least-squares line:');
fprintf(' Slope (m) = %8.3f\n', slope);
fprintf(' Intercept (b) = %8.3f\n', y_int);
fprintf(' No. of points = %8d\n', n_points);

% Plot the data points as blue circles
plot(x, y, 'bo');
hold on;

% Create the fitted line
xmin = min(x);
xmax = max(x);
ymin = slope * xmin + y_int;
ymax = slope * xmax + y_int;

% Plot a solid red line
plot([xmin xmax], [ymin ymax], 'r-', 'LineWidth', 2);
hold off;

% Add title and legend
title('\bfLeast-Squares Fit');
xlabel('\bf\itx');
ylabel('\bf\ity');
legend('Input data', 'Fitted line');
grid on;
