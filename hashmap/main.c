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
    ht_set_entry(hashtable, "mykey", 12);
    ht_set_entry(hashtable, "asdf", 12);
    ht_set_entry(hashtable, "sdfg", 12);
    ht_set_entry(hashtable, "jklh", 12);
    ht_set_entry(hashtable, "qwer", 12);
    ht_set_entry(hashtable, "yuio", 12);
    ht_set_entry(hashtable, "dfgh", 12);
    ht_set_entry(hashtable, "zxcv", 12);
    ht_set_entry(hashtable, "xcvb", 12);
    ht_set_entry(hashtable, "rtyu", 12);
    ht_set_entry(hashtable, "fghj", 12);
    ht_set_entry(hashtable, "cvbn", 12);
    ht_set_entry(hashtable, "xcvb", 12);
    ht_set_entry(hashtable, "vbnm", 12);
    ht_set_entry(hashtable, "dsfg", 12);
    ht_set_entry(hashtable, "hgfd", 12);
    ht_set_entry(hashtable, "jhgf", 12);
    // ht_set_entry(hashtable, "jhif", 12);
    printf("%ld\n", hashtable->capacity);
    printf("%ld\n", hashtable->length);
    printf("%ld\n", hashtable->length);
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
