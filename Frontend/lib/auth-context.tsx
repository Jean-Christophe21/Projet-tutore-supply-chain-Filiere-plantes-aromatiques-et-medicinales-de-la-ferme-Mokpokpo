"use client"

import type React from "react"

import { createContext, useContext, useState, useEffect } from "react"
import { ApiService, ApiError } from "./api-service"

interface User {
  id_utilisateur: number
  email: string
  nom: string
  prenom: string
  role: "CLIENT" | "GEST_COMMERCIAL" | "GEST_STOCK" | "ADMIN"
}

interface AuthContextType {
  user: User | null
  isLoading: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

// Helper to decode JWT token
function parseJwt(token: string): any {
  try {
    const base64Url = token.split(".")[1]
    const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/")
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split("")
        .map((c) => "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2))
        .join("")
    )
    return JSON.parse(jsonPayload)
  } catch (error) {
    return null
  }
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  // Initialize from localStorage on mount
  useEffect(() => {
    const initAuth = async () => {
      const storedToken = localStorage.getItem("mokpokpo_token")
      const storedUser = localStorage.getItem("mokpokpo_user")
      
      if (storedToken && storedUser) {
        try {
          const userData = JSON.parse(storedUser)
          // Verify token is still valid by making a test request
          await ApiService.getUser(userData.id_utilisateur)
          setUser(userData)
        } catch (error) {
          // Token expired or invalid, clear storage
          localStorage.removeItem("mokpokpo_token")
          localStorage.removeItem("mokpokpo_user")
        }
      }
      setIsLoading(false)
    }
    
    initAuth()
  }, [])

  const login = async (email: string, password: string) => {
    setIsLoading(true)
    
    try {
      // Call the real API
      const response = await ApiService.login(email, password)
      const token = response.access_token
      
      // Store the token
      localStorage.setItem("mokpokpo_token", token)
      
      // Decode token to get user info
      const payload = parseJwt(token)
      
      if (payload && payload.sub) {
        // Fetch full user details
        const userData = await ApiService.getUser(parseInt(payload.sub))
        
        const newUser: User = {
          id_utilisateur: userData.id_utilisateur,
          email: userData.email,
          nom: userData.nom,
          prenom: userData.prenom,
          role: userData.role,
        }
        
        setUser(newUser)
        localStorage.setItem("mokpokpo_user", JSON.stringify(newUser))
      }
    } catch (error) {
      // Re-throw the error so the login component can display it
      throw error
    } finally {
      setIsLoading(false)
    }
  }

  const logout = () => {
    setUser(null)
    localStorage.removeItem("mokpokpo_token")
    localStorage.removeItem("mokpokpo_user")
  }

  return <AuthContext.Provider value={{ user, isLoading, login, logout }}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error("useAuth must be used within AuthProvider")
  }
  return context
}
