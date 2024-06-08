#ifndef EXPORT_H
#define EXPORT_H

#if defined(_WIN32) && defined(BUILDING_SHARED)
	#define EXPORT __declspec(dllexport)
#else
	#define EXPORT extern
#endif

#endif
