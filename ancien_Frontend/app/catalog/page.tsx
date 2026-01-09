"use client"

import { useState, useEffect } from "react"
import Link from "next/link"
import { Header } from "@/components/header"
import { Footer } from "@/components/footer"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Search } from "lucide-react"
import { ApiService } from "@/lib/api-service"

interface Product {
  id_produit: number
  nom_produit: string
  type_produit?: string
  prix_unitaire: number
  description?: string
  usages?: string
}

const categories = [
  { value: "MEDICINALE", label: "Plantes Médicinales" },
  { value: "AROMATIQUE", label: "Herbes Aromatiques" },
]

export default function CatalogPage() {
  const [products, setProducts] = useState<Product[]>([])
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [searchQuery, setSearchQuery] = useState("")
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    loadProducts()
  }, [])

  const loadProducts = async () => {
    try {
      setIsLoading(true)
      const data = await ApiService.getProducts()
      setProducts(data)
    } catch (err: any) {
      setError(err?.detail || "Erreur lors du chargement des produits")
    } finally {
      setIsLoading(false)
    }
  }

  const filteredProducts = products.filter((product) => {
    const matchCategory = !selectedCategory || product.type_produit === selectedCategory
    const matchSearch = product.nom_produit.toLowerCase().includes(searchQuery.toLowerCase())
    return matchCategory && matchSearch
  })

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1">
        <div className="container mx-auto px-4 py-12">
          <div className="mb-12">
            <h1 className="text-4xl font-bold text-foreground mb-4">Catalogue Complet</h1>
            <p className="text-muted-foreground text-lg">Découvrez toutes nos plantes et produits naturels</p>
          </div>

          {error && (
            <div className="mb-6 p-4 bg-destructive/10 border border-destructive/30 rounded-lg">
              <p className="text-destructive">{error}</p>
            </div>
          )}

          <div className="grid md:grid-cols-4 gap-6 mb-8">
            <div className="md:col-span-1">
              <div className="sticky top-20">
                <h3 className="font-semibold text-foreground mb-4">Catégories</h3>
                <div className="space-y-2">
                  <button
                    onClick={() => setSelectedCategory(null)}
                    className={`block w-full text-left px-4 py-2 rounded-md transition-colors ${
                      selectedCategory === null
                        ? "bg-primary text-primary-foreground"
                        : "text-foreground hover:bg-muted"
                    }`}
                  >
                    Tous les produits
                  </button>
                  {categories.map((cat) => (
                    <button
                      key={cat.value}
                      onClick={() => setSelectedCategory(cat.value)}
                      className={`block w-full text-left px-4 py-2 rounded-md transition-colors ${
                        selectedCategory === cat.value
                          ? "bg-primary text-primary-foreground"
                          : "text-foreground hover:bg-muted"
                      }`}
                    >
                      {cat.label}
                    </button>
                  ))}
                </div>
              </div>
            </div>

            <div className="md:col-span-3">
              <div className="mb-8">
                <div className="relative">
                  <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-muted-foreground" />
                  <input
                    type="text"
                    placeholder="Rechercher une plante..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full pl-10 pr-4 py-3 border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                  />
                </div>
              </div>

              {isLoading ? (
                <div className="text-center py-12">
                  <p className="text-muted-foreground">Chargement des produits...</p>
                </div>
              ) : (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                  {filteredProducts.length > 0 ? (
                    filteredProducts.map((product) => (
                      <Link key={product.id_produit} href={`/catalog/${product.id_produit}`}>
                        <Card className="h-full flex flex-col hover:shadow-lg transition-shadow cursor-pointer overflow-hidden">
                          <div className="relative w-full h-48 bg-muted">
                            <div className="w-full h-full flex items-center justify-center">
                              <p className="text-muted-foreground">Image produit</p>
                            </div>
                          </div>
                          <div className="p-4 flex flex-col flex-1">
                            <h3 className="font-semibold text-foreground mb-2">{product.nom_produit}</h3>
                            {product.type_produit && (
                              <span className="inline-block px-2 py-1 text-xs bg-primary/10 text-primary rounded mb-2">
                                {product.type_produit}
                              </span>
                            )}
                            <p className="text-sm text-muted-foreground mb-4 flex-1">
                              {product.description || product.usages || "Découvrez ce produit de qualité"}
                            </p>
                            <div className="flex items-center justify-between">
                              <span className="text-lg font-bold text-primary">
                                {Number(product.prix_unitaire).toLocaleString("fr-BJ")} FCFA
                              </span>
                              <Button
                                size="sm"
                                onClick={(e) => {
                                  e.preventDefault()
                                  // Will redirect to login if not authenticated
                                }}
                              >
                                Commander
                              </Button>
                            </div>
                          </div>
                        </Card>
                      </Link>
                    ))
                  ) : (
                    <div className="col-span-full text-center py-12">
                      <p className="text-muted-foreground">Aucun produit ne correspond à votre recherche</p>
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  )
}
