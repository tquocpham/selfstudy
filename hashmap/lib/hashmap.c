#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashmap.h"

unsigned long hash_function(char *str)
{
    unsigned long hash = 5381;
    int c;
    while ((c = *str++))
    {
        hash = ((hash << 5) + hash) + c;
    }
    return hash;
}

void print_htentry(HashTableEntry entry)
{
    printf("%s: %d\n", entry.key, entry.value);
}

void print_ht(HashTable *table)
{
    for (int i = 0; i < table->capacity; i++)
    {
        HashTableEntry *e = &table->entries[i];
        printf("%d %s: %d\n", i, e->key, e->value);
    }
}

struct HashTable *ht_create()
{
    // Allocate space for hash table struct.
    struct HashTable *table = malloc(sizeof(struct HashTable));
    if (table == NULL)
    {
        return NULL;
    }
    table->length = 0;
    table->capacity = 16;

    // Allocate (zero'd) space for entry buckets.
    table->entries = calloc(table->capacity, sizeof(struct HashTableEntry));
    if (table->entries == NULL)
    {
        free(table); // error, free table before we return!
        return NULL;
    }
    return table;
}

void ht_destroy(struct HashTable *table)
{
    // First free allocated keys.
    for (size_t i = 0; i < table->capacity; i++)
    {
        free((void *)table->entries[i].key);
    }

    // Then free entries array and table itself.
    free(table->entries);
    free(table);
}

// Internal function to set an entry (without expanding table).
char *ht_set_entry(struct HashTable *table, char *key, int value)
{
    size_t capacity = table->capacity;
    struct HashTableEntry *entries = table->entries;
    size_t *plength = &table->length;
    uint64_t hash = hash_function(key);
    // AND hash with capacity-1 to ensure it's within entries array.
    size_t index = (size_t)(hash & (uint64_t)(capacity - 1));

    //     // If length will exceed half of current capacity, expand it.
    //     // if (table->length >= table->capacity / 2)
    //     // {
    //     //     if (!ht_expand(table))
    //     //     {
    //     //         return NULL;
    //     //     }
    //     // }

    // Loop till we find an empty entry.
    while (entries[index].key != NULL)
    {
        if (strcmp(key, entries[index].key) == 0)
        {
            // Found key (it already exists), update value.
            entries[index].value = value;
            return entries[index].key;
        }
        // Key wasn't in this slot, move to next (linear probing).
        printf("hash collision detected %s %ld\n", key, index);
        index++;
        if (index >= capacity)
        {
            // At end of entries array, wrap around.
            index = 0;
        }
    }

    (*plength)++; // increment length

    entries[index].key = (char *)strdup(key);
    entries[index].value = value;
    struct HashTableEntry e = entries[index];
    printf("idx: %ld\n", index);
    // print_htentry(e);s
    // print_ht(table);
    return key;
}
