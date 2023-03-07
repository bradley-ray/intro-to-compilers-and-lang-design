#include <stdio.h>
#include <stdlib.h>
#include "json-scanner.h"

#define SIZE 1024


int main(void)
{
	token_vec* tokens = scan_for_tokens(NULL);

	free_token_vec(tokens);
	return 0;
}

// TODO: implement scanner
token_vec* scan_for_tokens(char* f) {
	token_vec* tokens = new_token_vec();

	return tokens;
}

void token_push(token_vec* tokens, token t) {
	if (tokens->len + 1 > tokens->size) {
		size_t prev_size = sizeof(token)*tokens->size;
		size_t added_size = sizeof(token)*SIZE;
		tokens->tokens = realloc(tokens->tokens, prev_size + added_size);
		if (tokens->tokens == NULL) {
			free_token_vec(tokens);
			printf("failed to reallocate token_vec->tokens");
			exit(1);
		}
		tokens->size += SIZE;
	}

	tokens->tokens[tokens->len++] = t;
}

token_vec* new_token_vec() {
	token_vec* tokens = (token_vec*)malloc(sizeof(token_vec));
	if (tokens == NULL) {
		free_token_vec(tokens);
		printf("failed to allocate token_vec");
		exit(1);
	}

	tokens->tokens = (token*)malloc(sizeof(token)*SIZE);
	if (tokens->tokens == NULL) {
		free_token_vec(tokens);
		printf("failed to allocate token_vec->tokens");
		exit(1);
	}

	tokens->size = SIZE;
	tokens->len = 0;

	return tokens;
}

void free_token_vec(token_vec* tokens) {
	free(tokens->tokens);
	free(tokens);
}
