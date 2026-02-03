#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "hashmap.h"

// Return 64-bit FNV-1a hash for key (NUL-terminated). See description:
// https://en.wikipedia.org/wiki/Fowler–Noll–Vo_hash_function
static uint64_t fnv1_hash_key(const char *key)
{
    uint64_t hash = FNV_OFFSET;
    for (const char *p = key; *p; p++)
    {
        hash ^= (uint64_t)(unsigned char)(*p);
        hash *= FNV_PRIME;
    }
    return hash;
}

unsigned long basic_hash_function(const char *str)
{
    unsigned long hash = 5381;
    int c;
    while ((c = *str++))
    {
        hash = ((hash << 5) + hash) + c;
    }
    return hash;
}

uint64_t hash_function(const char *str)
{
    // return basic_hash_function(char *str)
    return fnv1_hash_key(str);
}

void print_htentry(HashTableEntry entry)
{
    printf("%s: %p\n", entry.key, entry.value);
}

void print_ht(HashTable *table)
{
    for (int i = 0; i < table->capacity; i++)
    {
        HashTableEntry *e = &table->entries[i];
        printf("%d %s: %p\n", i, e->key, e->value);
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

// Expand hash table to twice its current size. Return true on success,
// false if out of memory.
static bool ht_expand(HashTable *table)
{
    // Allocate new entries array.
    size_t new_capacity = table->capacity * 2;
    if (new_capacity < table->capacity)
    {
        return false; // overflow (capacity would be too big)
    }
    HashTableEntry *new_entries = calloc(new_capacity, sizeof(HashTableEntry));
    if (new_entries == NULL)
    {
        return false;
    }

    // Iterate entries, move all non-empty ones to new table's entries.
    for (size_t i = 0; i < table->capacity; i++)
    {
        HashTableEntry entry = table->entries[i];
        if (entry.key != NULL)
        {
            ht_set_entry(new_entries, new_capacity, entry.key, entry.value, NULL);
        }
    }

    // Free old entries array and update this table's details.
    free(table->entries);
    table->entries = new_entries;
    table->capacity = new_capacity;
    return true;
}

// Internal function to set an entry (without expanding table).
static const char *ht_set_entry(HashTableEntry *entries, size_t capacity, const char *key, void *value, size_t *plength)
{
    // AND hash with capacity-1 to ensure it's within entries array.
    uint64_t hash = hash_function(key);
    size_t index = (size_t)(hash & (uint64_t)(capacity - 1));

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
        index++;

        // At end of entries array, wrap around.
        if (index >= capacity)
        {
            index = 0;
        }
    }

    // Didn't find key, allocate+copy if needed, then insert it.
    if (plength != NULL)
    {
        key = strdup(key);
        if (key == NULL)
        {
            return NULL;
        }
        (*plength)++;
    }
    entries[index].key = (char *)key;
    entries[index].value = value;
    return key;
}

// Internal function to set an entry (without expanding table).
const char *ht_set(struct HashTable *table, const char *key, void *value)
{
    size_t capacity = table->capacity;
    struct HashTableEntry *entries = table->entries;
    size_t *plength = &table->length;
    uint64_t hash = hash_function(key);
    // AND hash with capacity-1 to ensure it's within entries array.
    size_t index = (size_t)(hash & (uint64_t)(capacity - 1));

    // If length will exceed half of current capacity, expand it.
    if (table->length >= table->capacity / 2)
    {
        if (!ht_expand(table))
        {
            return NULL;
        }
    }

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

void *ht_get(HashTable *table, const char *key)
{
    // AND hash with capacity-1 to ensure it's within entries array.
    uint64_t hash = hash_function(key);
    printf("hash: %llu\n", hash);
    size_t index = (size_t)(hash & (uint64_t)(table->capacity - 1));
    printf("idx: %zu\n", index);

    // Loop till we find an empty entry.
    while (table->entries[index].key != NULL)
    {
        char *k = table->entries[index].key;
        printf("k: %s\n", k);
        if (strcmp(key, table->entries[index].key) == 0)
        {
            // Found key, return value.
            return table->entries[index].value;
        }
        // Key wasn't in this slot, move to next (linear probing).
        index++;
        if (index >= table->capacity)
        {
            // At end of entries array, wrap around.
            index = 0;
        }
    }
    return NULL;
}
