function [index, error] = findnearest(element, sequence)
absError = abs(sequence - element);
[error, index] = min(absError);
end