# Guide de Contribution - Projet Mokpokpo

Merci de votre intérêt pour contribuer au projet Mokpokpo ! Ce guide vous aidera à contribuer efficacement.

## ?? Table des Matières

1. [Code de Conduite](#code-de-conduite)
2. [Comment Contribuer](#comment-contribuer)
3. [Standards de Code](#standards-de-code)
4. [Workflow Git](#workflow-git)
5. [Tests](#tests)
6. [Documentation](#documentation)

## ?? Code de Conduite

- Soyez respectueux et professionnel
- Écoutez et acceptez les critiques constructives
- Concentrez-vous sur ce qui est meilleur pour le projet
- Faites preuve d'empathie envers les autres membres

## ?? Comment Contribuer

### Rapporter un Bug

1. Vérifiez que le bug n'a pas déjà été rapporté
2. Créez une issue avec le label `bug`
3. Incluez:
   - Description claire du problème
   - Étapes pour reproduire
   - Comportement attendu vs actuel
   - Captures d'écran si pertinent
   - Version du système/navigateur

### Proposer une Fonctionnalité

1. Créez une issue avec le label `enhancement`
2. Décrivez:
   - Le problème que ça résout
   - La solution proposée
   - Les alternatives considérées
   - L'impact sur l'existant

### Soumettre une Pull Request

1. Forkez le dépôt
2. Créez une branche depuis `main`:
   ```bash
   git checkout -b feature/ma-fonctionnalite
   ```
3. Faites vos modifications
4. Écrivez ou mettez à jour les tests
5. Assurez-vous que tous les tests passent
6. Commitez vos changements:
   ```bash
   git commit -m "feat: ajoute nouvelle fonctionnalité X"
   ```
7. Poussez vers votre fork:
   ```bash
   git push origin feature/ma-fonctionnalite
   ```
8. Ouvrez une Pull Request

## ?? Standards de Code

### Backend (Python)

#### Style
- Suivre PEP 8
- Utiliser des noms de variables explicites
- Limiter les lignes à 88 caractères (Black formatter)
- Utiliser des docstrings pour les fonctions/classes

#### Exemple
```python
from typing import Optional
from sqlalchemy.orm import Session

def get_user_by_email(db: Session, email: str) -> Optional[Utilisateur]:
    """
    Récupère un utilisateur par son email.
    
    Args:
        db: Session de base de données
        email: Email de l'utilisateur
        
    Returns:
        L'utilisateur si trouvé, None sinon
    """
    return db.query(Utilisateur).filter(Utilisateur.email == email).first()
```

#### Structure des Endpoints
```python
@router.post("/", response_model=Schema, dependencies=[Depends(RoleChecker([...]))])
def create_resource(data: CreateSchema, db: Session = Depends(get_db)):
    """Description de l'endpoint."""
    # 1. Validations
    if not condition:
        raise HTTPException(status_code=400, detail="Message")
    
    # 2. Logique métier
    resource = Model(**data.model_dump())
    
    # 3. Sauvegarde
    try:
        db.add(resource)
        db.commit()
        db.refresh(resource)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Erreur")
    
    return resource
```

### Frontend (TypeScript/React)

#### Style
- Utiliser TypeScript strict
- Préférer les functional components
- Utiliser des hooks pour la logique
- Nommer les composants en PascalCase
- Nommer les fichiers en kebab-case

#### Exemple de Composant
```typescript
"use client"

import { useState, useEffect } from "react"
import { ApiService } from "@/lib/api-service"
import type { Product } from "@/lib/types"

interface ProductListProps {
  category?: string
}

export function ProductList({ category }: ProductListProps) {
  const [products, setProducts] = useState<Product[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    loadProducts()
  }, [category])

  const loadProducts = async () => {
    try {
      setIsLoading(true)
      const data = await ApiService.getProducts()
      setProducts(data)
    } catch (err) {
      setError("Erreur de chargement")
    } finally {
      setIsLoading(false)
    }
  }

  if (isLoading) return <div>Chargement...</div>
  if (error) return <div>{error}</div>

  return (
    <div>
      {products.map((product) => (
        <ProductCard key={product.id_produit} product={product} />
      ))}
    </div>
  )
}
```

#### Structure des Services
```typescript
export class ApiService {
  private static async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    // Gestion des headers, auth, erreurs
  }

  static async getResource(id: number): Promise<Resource> {
    return this.request(`/resources/${id}`)
  }

  static async createResource(data: CreateData): Promise<Resource> {
    return this.request("/resources", {
      method: "POST",
      body: JSON.stringify(data),
    })
  }
}
```

## ?? Workflow Git

### Branches

- `main` : Code stable en production
- `develop` : Code de développement
- `feature/nom` : Nouvelles fonctionnalités
- `fix/nom` : Corrections de bugs
- `hotfix/nom` : Corrections urgentes

### Messages de Commit

Utilisez le format Conventional Commits:

```
<type>(<scope>): <description>

[corps optionnel]

[footer optionnel]
```

**Types:**
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation uniquement
- `style`: Formatage, points-virgules, etc.
- `refactor`: Refactorisation du code
- `test`: Ajout ou modification de tests
- `chore`: Maintenance, dépendances

**Exemples:**
```bash
feat(auth): ajoute la connexion par email
fix(catalog): corrige le filtrage par catégorie
docs(readme): met à jour le guide d'installation
style(frontend): applique prettier sur les composants
refactor(api): optimise les requêtes de produits
test(backend): ajoute tests pour les commandes
chore(deps): met à jour fastapi vers 0.104.0
```

## ? Tests

### Backend

#### Tests Unitaires
```python
# tests/test_product.py
import pytest
from models.model import Produit

def test_create_product(db):
    """Test la création d'un produit."""
    product = Produit(
        nom_produit="Test",
        prix_unitaire=1000
    )
    db.add(product)
    db.commit()
    
    assert product.id_produit is not None
    assert product.nom_produit == "Test"
```

#### Tests d'Endpoints
```python
def test_get_products(client):
    """Test GET /produits."""
    response = client.get("/produits")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

#### Exécuter les Tests
```bash
cd Backend
pytest
pytest --cov=. --cov-report=html
```

### Frontend

#### Tests de Composants
```typescript
// __tests__/ProductCard.test.tsx
import { render, screen } from "@testing-library/react"
import { ProductCard } from "@/components/ProductCard"

describe("ProductCard", () => {
  it("affiche le nom du produit", () => {
    const product = {
      id_produit: 1,
      nom_produit: "Test",
      prix_unitaire: 1000,
    }
    
    render(<ProductCard product={product} />)
    expect(screen.getByText("Test")).toBeInTheDocument()
  })
})
```

#### Exécuter les Tests
```bash
cd Frontend
npm test
npm run test:coverage
```

## ?? Documentation

### Docstrings (Python)
```python
def function_name(param1: Type1, param2: Type2) -> ReturnType:
    """
    Description courte de la fonction.
    
    Description détaillée si nécessaire, expliquant le comportement,
    les cas particuliers, etc.
    
    Args:
        param1: Description du paramètre 1
        param2: Description du paramètre 2
        
    Returns:
        Description de la valeur de retour
        
    Raises:
        ValueError: Si param1 est invalide
        HTTPException: Si ressource non trouvée
        
    Example:
        >>> result = function_name("test", 42)
        >>> print(result)
        "résultat"
    """
    pass
```

### JSDoc (TypeScript)
```typescript
/**
 * Charge la liste des produits depuis l'API.
 * 
 * @param category - Catégorie optionnelle pour filtrer
 * @returns Promise contenant la liste des produits
 * @throws {ApiError} Si l'API retourne une erreur
 * 
 * @example
 * ```typescript
 * const products = await loadProducts("MEDICINALE")
 * ```
 */
async function loadProducts(category?: string): Promise<Product[]> {
  // ...
}
```

### README pour Nouveaux Modules

Chaque nouveau module important doit avoir un README:

```markdown
# Module Name

Brève description.

## Installation

Instructions d'installation.

## Usage

Exemples d'utilisation.

## API

Liste des fonctions/classes publiques.

## Tests

Comment exécuter les tests.
```

## ?? Checklist Pull Request

Avant de soumettre une PR, assurez-vous que:

- [ ] Le code suit les standards du projet
- [ ] Les tests passent (backend et frontend)
- [ ] La couverture de tests n'a pas diminué
- [ ] La documentation est à jour
- [ ] Les commits suivent le format Conventional Commits
- [ ] Pas de `console.log` ou `print` de debug
- [ ] Pas de fichiers sensibles (`.env`, credentials)
- [ ] Le code est formaté (Black pour Python, Prettier pour TS)
- [ ] Pas de warnings dans les linters

## ?? Revue de Code

### Pour les Reviewers

- Vérifiez la logique et la clarté du code
- Suggérez des améliorations plutôt que d'imposer
- Validez que les tests couvrent les cas limites
- Assurez-vous que la documentation est claire
- Testez localement si nécessaire

### Pour les Auteurs

- Soyez ouvert aux commentaires
- Répondez aux questions et suggestions
- Mettez à jour la PR selon les retours
- Marquez les conversations comme résolues
- Testez après chaque modification

## ?? Communication

- **Issues**: Pour bugs, fonctionnalités, questions
- **Pull Requests**: Pour proposer des changements
- **Discussions**: Pour idées et débats

## ?? Besoin d'Aide?

- Consultez la [documentation](./INTEGRATION_GUIDE.md)
- Ouvrez une issue avec le label `question`
- Contactez les mainteneurs

## ?? Remerciements

Merci pour votre contribution au projet Mokpokpo !

---

**Dernière mise à jour**: 07/01/2026
