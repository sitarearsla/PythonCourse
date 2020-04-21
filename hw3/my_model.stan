data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  vector[N] x;
  vector[N] c;
  vector[N] y;
} 
parameters {
  vector[J] a;
  vector[2] b;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 
transformed parameters {
  vector[N] m;
  vector[N] y_hat;
  for (i in 1:N) {
   m[i] = a[country[i]] + c[i] * b[1];
   y_hat[i] = m[i] + x[i] * b[2];
    }
}
model {
  sigma_y ~ uniform(0, 100);
  sigma_a ~ uniform(0, 100);
  mu_a ~ normal(0, 10);
  a ~ normal(mu_a, sigma_a);
  b ~ normal(0, 10);
  y ~ normal(y_hat, sigma_y);
}
