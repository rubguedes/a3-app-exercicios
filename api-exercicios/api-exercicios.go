package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/gorilla/mux"
)

// Estruturando e definindo o tipo de dado dos atributos de cada exercício.
type Exercicio struct {
	Uuid       string
	Nome       string
	Repeticoes string
	Descricao  string
}

// Estruturando a lista de Treinos, será uma lista com vários Treinos.
type Exercicios struct {
	Exercicios []Exercicio
}

// Abrindo o arquivo json e lendo o arquivo.
func loadData() []byte {
	jsonFile, err := os.Open("lista-exercicios.json")
	//Verifica se há algum erro no arquivo.
	if err != nil {
		fmt.Printf("Error: " + err.Error())
	}
	//Fechando o arquivo
	defer jsonFile.Close()

	data, _ := os.ReadFile("lista-exercicios.json")
	return data
}

func ListaExercicios(w http.ResponseWriter, r *http.Request) {
	//A variável exercicios está recebendo os dados carregados pela função loadData.
	exercicios := loadData()
	//Os dados da variável treinos está sendo escrito via http.
	w.Write([]byte(exercicios))
}

func InserirExercicios(w http.ResponseWriter, r *http.Request) {
	var exercicio Exercicio
    err := json.NewDecoder(r.Body).Decode(&exercicio)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    // Retorna a resposta
    w.WriteHeader(http.StatusCreated)
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(exercicio)
}

func GetExercicioById(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	data := loadData()

	var exercicios Exercicios
	json.Unmarshal(data, &exercicios)

	for _, v := range exercicios.Exercicios {
		if v.Uuid == vars["id"] {
			exercicio, _ := json.Marshal(v)
			w.Write([]byte(exercicio))
		}
	}
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/exercicios", ListaExercicios)
	r.HandleFunc("/exercicio/{id}", GetExercicioById)
	r.HandleFunc("/exercicios/inserir-exercicios", InserirExercicios).Methods("POST")
	http.ListenAndServe(":8000", r)
}
