#ifndef HASH_TABLE_H
#define HASH_TABLE_H

// The FNV_offset_basis is the 64-bit value: 14695981039346656037 (in hex, 0xcbf29ce484222325).
// The FNV_prime is the 64-bit value 1099511628211 (in hex, 0x100000001b3)..
#define FNV_OFFSET 14695981039346656037UL
#define FNV_PRIME 1099511628211UL

// Struct and typedef declarations
struct HashTableEntry
{
    char *key;
    void *value;
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
void ht_destroy(HashTable *table);
// unsigned long hash_function(char *str);
uint64_t hash_function(const char *str);
static const char *ht_set_entry(HashTableEntry *entries, size_t capacity, const char *key, void *value, size_t *plength);
void *ht_get(HashTable *table, const char *key);
const char *ht_set(HashTable *table, const char *key, void *value);
void print_htentry(HashTableEntry entry);
void print_ht(HashTable *table);

#endif // HASH_TABLE_H
