// Consolidated and optimized JavaScript for NextGen Scholars website
document.addEventListener("DOMContentLoaded", function () {
  // DOM Elements
  const navbar = document.querySelector(".navbar");
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");
  const body = document.body;

  // Only proceed if elements exist
  if (!navbar) return;

  // Create overlay for mobile menu
  const overlay = document.createElement("div");
  overlay.className = "overlay";
  document.body.appendChild(overlay);

  // Mobile Menu Toggle
  function toggleMenu() {
    if (navLinks) {
      const isOpen = navLinks.classList.toggle("active");
      overlay.classList.toggle("active");
      body.classList.toggle("menu-open");

      // Update ARIA attribute for accessibility
      if (menuToggle) {
        menuToggle.setAttribute("aria-expanded", isOpen);
      }
    }
  }

  function closeMenu() {
    if (navLinks) {
      navLinks.classList.remove("active");
      overlay.classList.remove("active");
      body.classList.remove("menu-open");

      // Update ARIA attribute for accessibility
      if (menuToggle) {
        menuToggle.setAttribute("aria-expanded", "false");
      }
    }
  }

  // Menu toggle button click
  if (menuToggle) {
    menuToggle.addEventListener("click", toggleMenu);
  }

  // Overlay click to close menu
  overlay.addEventListener("click", closeMenu);

  // Close menu when clicking on links
  if (navLinks) {
    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", closeMenu);
    });
  }

  // Close menu when clicking outside
  document.addEventListener("click", function (e) {
    if (navLinks && menuToggle) {
      const isClickInsideNav = navLinks.contains(e.target);
      const isClickInsideToggle = menuToggle.contains(e.target);

      if (
        !isClickInsideNav &&
        !isClickInsideToggle &&
        navLinks.classList.contains("active")
      ) {
        closeMenu();
      }
    }
  });

  // Scroll behavior for navbar
  let lastScrollTop = 0;

  window.addEventListener("scroll", function () {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    // Add shadow and background opacity based on scroll position
    if (scrollTop > 10) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }

    // Hide/show navbar based on scroll direction
    if (scrollTop > lastScrollTop && scrollTop > 300) {
      // Scrolling down & past threshold
      navbar.classList.add("navbar-hidden");
    } else {
      // Scrolling up
      navbar.classList.remove("navbar-hidden");
    }

    lastScrollTop = scrollTop;
  });

  // Highlight current page in navigation
  if (navLinks) {
    const currentPage = window.location.pathname.split("/").pop() || "index.html";
    const currentLocation = window.location.href;

    navLinks.querySelectorAll("a").forEach((link) => {
      // Check both href attribute and full location
      if (link.getAttribute("href") === currentPage || link.href === currentLocation) {
        link.classList.add("active");
      }
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href");

      // Skip if just "#"
      if (targetId === "#") return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();

        const navbarHeight = navbar.offsetHeight || 0;
        const targetPosition =
          targetElement.getBoundingClientRect().top +
          window.pageYOffset -
          navbarHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: "smooth",
        });
      }
    });
  });

  // Lazy loading for images
  if ("IntersectionObserver" in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const img = entry.target;
          if (img.dataset.src) {
            img.src = img.dataset.src;
            img.removeAttribute("data-src");
          }
          imageObserver.unobserve(img);
        }
      });
    });

    // Observe all images with data-src attribute
    document.querySelectorAll("img[data-src]").forEach((img) => {
      imageObserver.observe(img);
    });
  }
});
