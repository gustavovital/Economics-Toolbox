white.test <- function(modelo, significancia = 0.05){

	## defini dois argumentos, o modelo a ser testado, e
	## o nível de signific^ancia do teste, que por defaut
	## está 5%

	## defino os resíduos^2 e a partir da classe lm eu
	## construo um dataframe para as variáveis exógenas
	## do da regressão a ser realizada
	
	u_hat2 <- resid(modelo)^2
	data.mod <- data.frame(modelo$model)
	exog <- attr(modelo$terms, "term.labels")
	data <- data.frame(u_hat2, data.mod[exog])
	
	## defino por fim o 'n' do modelo, e a matriz de regressores
	## sendo elas as variáveis explicativas, as variáveis explicativas
	## ao quadrado, e as interações entre as variáveis explicativas
	
	n <- nrow(data)
	matrix.white <- as.matrix(data.frame(model.matrix(u_hat2 ~ . + .^2, data = data), 
		data.mod[exog]^2))[, -1]

	reg.white <- lm(u_hat2 ~ matrix.white)
	nr2 <- n*summary(reg.white)$r.squared
	
	x2 <- qchisq(1 - significancia, reg.white[[rank]]-1)
	significancia <- as.character(significancia*100)
	pvalueWhite <- paste("P-Valor =", as.character(1-pchisq(nr2, reg.white[[rank]]-1)))

	## organizo as saidas do teste
	if(nr2 > x2){
		strn <- paste("Rejeitamos H0 a", significancia, '%')
	} else{
		strn <- paste("Não rejeitamos H0 a", significancia, '%')	
	}
	
	nr2 <- as.character(nr2)
	x2 <- as.character(x2)
	hip1 <- 'H0 : HOMOCEDASTICIDADE'
	hip2 <- 'H1 : AUSÊNCIA DE HOMOCEDASTICIDADE'

	nr2 <- paste("Estatística de Teste:", nr2)
	x2 <- paste("Região Crítica:", x2)
	grade <- '________________________________________'

	return(cat(c(grade, 'Teste de White Para Heterocedasticidade','',
		hip1, hip2,'', strn, nr2, x2, pvalueWhite, grade), sep = "nn"))
}
