#include <stdio.h>
#define BUF_SZ 1024

// structure of our huffman node
typedef struct s_hnode {
    struct s_hnode *left;
    struct s_hnode *right;
    char data;
    int rank;
}   t_hnode;

typedef struct s_env {
    char **ref;
}   t_env;

t_env gl_env;

// O(n) time instead of O(log n)
void enqueue(t_hnode*, t_hnode, int);

void encode(t_hnode*);
void encode_r(t_hnode*, int);

void my_char(char);
void my_str(char*);
int my_strlen(char*);


char *to_bin(int);

int main(int argc, char **argv) {
    int fd, n, i;
    int n_nodes = 0;
    
    char *buff = (char*)malloc(BUF_SZ * sizeof(char));
    int *freq = (int*)malloc(256 * sizeof(int));
    t_hnode *nodes = (t_hnode*)malloc(256 * sizeof(t_hnode));
    
    gl_env.ref = (char**)malloc(256 * sizeof(char*));
    
    // read in our file in chunks
    fd = open(argv[1], 0);
    while ((n = read(fd, buff, BUF_SZ)) > 0)
        for (i = 0; i < n; i++)
            freq[buff[i]]++;
            
    close(fd);
    
    // create nodes for each byte used
    for (i = 0; i < 256; i++) {
        if (freq[i] != 0) {
            t_hnode my_node;
            
            my_node.data = i;
            my_node.rank = freq[i];
            my_node.left = NULL;
            my_node.right = NULL;
            
            
            enqueue(nodes, my_node, n_nodes);
            n_nodes++;
        }
    }
    
    // compress all nodes into a tree
    while (n_nodes > 1) {
        t_hnode a = nodes[--n_nodes];
        t_hnode b = nodes[--n_nodes];
        
        t_hnode combine;
        combine.left = (t_hnode*)malloc(sizeof(t_hnode));
        combine.left->data = a.data;
        combine.left->rank = a.rank;
        combine.left->left = a.left;
        combine.left->right = a.right;
        
        combine.right = (t_hnode*)malloc(sizeof(t_hnode));
        combine.right->data = b.data;
        combine.right->rank = b.rank;
        combine.right->left = b.left;
        combine.right->right = b.right;
        
        combine.rank = a.rank + b.rank;
        combine.data = 0;
        
        enqueue(nodes, combine, n_nodes);
        n_nodes++;
    }
    
    // populate gl_env.ref with codes for each character
    encode(nodes);
    
    int total = 0;
    
    // reread everything, but now print the encoded byte
    fd = open(argv[1], 0);
    while ((n = read(fd, buff, BUF_SZ)) > 0)
        for (i = 0; i < n; i++) {
            my_str(gl_env.ref[buff[i]]);
            total += my_strlen(gl_env.ref[buff[i]]);
        }
    
    close(fd);
            
    printf("\nLength: %d bits\n", total);
            
    free(nodes);
    free(freq);
    free(buff);
    //for (i = 0; i < 256; i++)
        //free(gl_env.ref[i]);
    free(gl_env.ref);
}

void enqueue(t_hnode *nodes, t_hnode my_node, int index) { 
    nodes[index] = my_node;
    while (index > 0) {
        if (nodes[index-1].rank < nodes[index].rank) {
            t_hnode temp_node = nodes[index-1];
            nodes[index-1] = nodes[index];
            nodes[index] = temp_node;
            
            index--;
        } else
            break;
    }
}

void encode(t_hnode* node) {
    encode_r(node->left, 1);
    encode_r(node->right, 2);
}

void encode_r(t_hnode* node, int k) {
    if (node->left == NULL) {
        char *bin = to_bin(k);
        gl_env.ref[node->data] = bin;
    } else {
        encode_r(node->left, (k * 10) + 1);
        encode_r(node->right, (k * 10) + 2);
    }
}

char *to_bin(int k) {
    int i;
    char *ret = (char*)malloc(9 * sizeof(char));
    
    for (i = 0; i < 9; i++)
        ret[i] = 0;
    
    i = 7;
    while (k > 0) {
        ret[i--] = (k % 10) - 1 + '0';
        k /= 10;
    }
    
    while (ret[0] == '\0')
        ret++;
        
    return ret;
}

int my_strlen(char *s) {
    int n;
    if (s == NULL)
        return 0;
    for (n = 0; s[n] != '\0'; n++) ;
    return n;
}

void my_str(char *s) {
    write(1, s, my_strlen(s));
}