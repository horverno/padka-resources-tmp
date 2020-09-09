i = 1;
file_name = sprintf('csv\\padka%03d.csv', i);
table = readtable(file_name);
points = table{:,:};
plot(points(2,:), points(3,:), 'go-.', 'DisplayName', file_name(5:end))
xlabel('x [meters]')
ylabel('y [meters] magassag')
title(file_name(5:end), 'Interpreter', 'none');
grid on
legend