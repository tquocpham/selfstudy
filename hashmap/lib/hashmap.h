#ifndef HASH_TABLE_H
#define HASH_TABLE_H

// // Global variable declarations (if necessary, often better to avoid)
// extern int global_variable;

// Struct and typedef declarations
struct HashTableEntry
{
    char *key;
    int value;
};
typedef struct HashTableEntry HashTableEntry;

// HashTable is a hash table structure:
// create with ht_create, free with ht_destroy.
struct HashTable
{
    struct HashTableEntry *entries; // hash slots
    size_t capacity;                // size of _entries array
    size_t length;                  // number of items in hash table
};
typedef struct HashTable HashTable;

// Function declarations
HashTable *ht_create();
unsigned long hash_function(char *str);
void ht_destroy(HashTable *table);
char *ht_set_entry(HashTable *table, char *key, int value);
void print_htentry(HashTableEntry entry);
void print_ht(HashTable *table);

#endif // HASH_TABLE_H
