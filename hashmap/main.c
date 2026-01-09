#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lib/hashmap.h"

int main()
{
    HashTable *hashtable = ht_create();
    printf("%ld\n", hashtable->capacity);
    printf("%ld\n", hashtable->length);
    printf("%ld\n", hashtable->length);
    ht_set(hashtable, "mykey", (void *)(intptr_t)1);
    ht_set(hashtable, "asdf", (void *)(intptr_t)2);
    ht_set(hashtable, "sdfg", (void *)(intptr_t)3);
    ht_set(hashtable, "jklh", (void *)(intptr_t)4);
    ht_set(hashtable, "qwer", (void *)(intptr_t)5);
    ht_set(hashtable, "yuio", (void *)(intptr_t)6);
    ht_set(hashtable, "dfgh", (void *)(intptr_t)7);
    ht_set(hashtable, "zxcv", (void *)(intptr_t)8);
    ht_set(hashtable, "xcvb", (void *)(intptr_t)9);
    ht_set(hashtable, "rtyu", (void *)(intptr_t)12);
    ht_set(hashtable, "fghj", (void *)(intptr_t)12);
    ht_set(hashtable, "cvbn", (void *)(intptr_t)12);
    ht_set(hashtable, "xcvb", (void *)(intptr_t)12);
    ht_set(hashtable, "vbnm", (void *)(intptr_t)12);
    ht_set(hashtable, "dsfg", (void *)(intptr_t)12);
    ht_set(hashtable, "hgfd", (void *)(intptr_t)12);
    ht_set(hashtable, "jhgf", (void *)(intptr_t)12);
    ht_set(hashtable, "jhif", (void *)(intptr_t)12);
    printf("%ld\n", hashtable->capacity);
    printf("%ld\n", hashtable->length);
    printf("%ld\n", hashtable->length);
    int result = (int)(intptr_t)ht_get(hashtable, "sdfg");
    printf("sdfg: Value: %d\n", result);
    printf("%ld\n", hashtable->capacity);
    print_ht(hashtable);
    ht_destroy(hashtable);
    // char string_name[] = "Your Text";
    // unsigned long hash = hash_function(string_name);
    // printf("%ld\n", hash);

    // char string_name2[] = "Yuor Txet";
    // unsigned long hash2 = hash_function(string_name2);
    // printf("%ld\n", hash2);
    return 0;
}
