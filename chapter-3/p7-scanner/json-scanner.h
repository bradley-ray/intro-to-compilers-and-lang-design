#ifndef JSONSCANNER
#define JSONSCANNER

// probably will need to change
typedef enum {
	JSON,
	ELEMENT,
	VALUE,
	OBJECT,
	ARRAY,
	STRING,
	NUMBER,
	WS,
	MEMBERS,
	MEMBER,
	ELEMENTS,
	CHARACTERS,
	CHARACTER,
	ESCAPE,
	HEX,
	INTEGER,
	DIGITS,
	DIGIT,
	ONENINE,
	FRACTION,
	EXPONENT,
	SIGN,
} token;

typedef struct {
	token* tokens;
	int size;
	int len;
} token_vec;

token_vec* scan_for_tokens(char* f);

token_vec* new_token_vec();
void free_token_vec(token_vec* t);

void token_push(token_vec* tokens, token t);

#endif
